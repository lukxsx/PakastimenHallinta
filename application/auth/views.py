from flask import render_template, request, redirect, url_for
from application import app
from application.auth.models import User
from application.auth.forms import LoginForm

@app.route("/auth/kirjaudu", methods = ["GET", "POST"])
def kirjautuminen():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Väärä käyttäjätunnus tai salasana")


    print("Käyttäjä " + user.name + " tunnistettiin")
    return redirect(url_for("elintarvike_listaus"))