from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.forms import LoginForm, CreateAccount
from application.auth.models import Kayttaja


@app.route("/auth/kirjaudu", methods=["GET", "POST"])
def kirjautuminen():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    user = Kayttaja.query.filter_by(tunnus=form.tunnus.data, salasana=form.salasana.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form,
                               error="Väärä käyttäjätunnus tai salasana")

    login_user(user)
    return redirect(url_for("index"))


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

    # luodaan käyttäjä
    k = Kayttaja(form.tunnus.data, form.salasana.data)
    db.session.add(k)
    db.session.commit()

    # kirjaudutaan sisään
    user = Kayttaja.query.filter_by(tunnus=form.tunnus.data, salasana=form.salasana.data).first()
    login_user(user)
    return redirect(url_for("index"))
