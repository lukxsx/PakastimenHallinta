from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from application import app, db, bcrypt
from application.auth.forms import LoginForm, CreateAccount
from application.auth.models import Kayttaja


@app.route("/auth/kirjaudu", methods=["GET", "POST"])
def kirjautuminen():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    kayttaja = Kayttaja.query.filter_by(tunnus=form.tunnus.data).first()

    # tarkistetaan, löytyykö käyttäjää tietokannasta
    if not kayttaja:
        return render_template("auth/loginform.html", form=form,
                               error="Väärä käyttäjätunnus tai salasana")

    # tarkistetaan salasanan hashaus
    salasana = form.salasana.data
    if bcrypt.check_password_hash(kayttaja.hash, salasana):
        login_user(kayttaja)
        return redirect(url_for("index"))
    else:
        return render_template("auth/loginform.html", form=form,
                               error="Väärä käyttäjätunnus tai salasana")


@app.route("/auth/ulos")
def uloskirjautuminen():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/uusikayttaja", methods=["GET", "POST"])
def kayttajan_luonti():
    if request.method == "GET":
        return render_template("auth/createaccount.html", form=CreateAccount())

    form = CreateAccount(request.form)

    # tarkistetaan, löytyykö käyttäjää jo tietokannasta
    user = Kayttaja.query.filter_by(tunnus=form.tunnus.data).first()
    if user:
        return render_template("auth/createaccount.html", form=form, error="Käyttäjätunnus on jo olemassa.")

    if not form.validate():
        return render_template("auth/createaccount.html", form=form)

    # hashataan salasana ja lisätään käyttäjä
    password = form.salasana.data
    pw_hash = bcrypt.generate_password_hash(password)
    k = Kayttaja(form.tunnus.data, pw_hash)
    db.session.add(k)
    db.session.commit()

    # kirjaudutaan sisään uudella käyttäjällä
    user = Kayttaja.query.filter_by(tunnus=form.tunnus.data).first()
    login_user(user)
    return redirect(url_for("index"))
