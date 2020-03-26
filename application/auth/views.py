from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from application import app
from application.auth.models import Kayttaja
from application.auth.forms import LoginForm

@app.route("/auth/kirjaudu", methods = ["GET", "POST"])
def kirjautuminen():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = Kayttaja.query.filter_by(tunnus=form.tunnus.data, salasana=form.salasana.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Väärä käyttäjätunnus tai salasana")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/ulos")
def uloskirjautuminen():
    logout_user()
    return redirect(url_for("index"))