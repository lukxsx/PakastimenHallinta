from application import app, db
from flask import redirect, render_template, request, url_for
from application.elintarvike.models import Elintarvike


@app.route("/elintarvikkeet", methods=["GET"])
def elintarvike_listaus():
    return render_template("elintarvikkeet/listaa.html", elintarvikkeet=Elintarvike.query.all())


@app.route("/elintarvikkeet/lisaa/")
def elintarvike_lisays():
    return render_template("elintarvikkeet/lisaa.html")


@app.route("/elintarvikkeet/", methods=["POST"])
def elintarvike_lisaaja():
    nimi = request.form.get("nimi")
    sailyvyys = request.form.get("sailyvyys")
    e = Elintarvike(nimi, sailyvyys)
    db.session().add(e)
    db.session().commit()

    return redirect(url_for("elintarvike_listaus"))
