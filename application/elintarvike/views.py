from application import app, db
from flask import redirect, render_template, request, url_for
from application.elintarvike.models import Elintarvike


@app.route("/elintarvikkeet", methods=["GET"])
def elintarvike_listaus():
    return render_template("elintarvikkeet/listaa.html", elintarvikkeet=Elintarvike.query.all())


@app.route("/elintarvikkeet/lisaa/")
def elintarvike_lisays():
    return render_template("elintarvikkeet/lisaa.html")


@app.route("/elintarvikkeet/<elintarvike_id>/", methods=["POST"])
def elintarvike_paivitys(elintarvike_id):
    elin = Elintarvike.query.get(elintarvike_id)
    elin.sailyvyys = request.form.get("uusi")
    db.session.commit()
    return redirect(url_for("elintarvike_listaus"))


@app.route("/elintarvikkeet/", methods=["POST"])
def elintarvike_lisaaja():
    nimi = request.form.get("nimi")
    s = request.form.get("sailyvyys")
    print(s)
    e = Elintarvike(nimi, s)
    db.session().add(e)
    db.session().commit()

    return redirect(url_for("elintarvike_listaus"))
