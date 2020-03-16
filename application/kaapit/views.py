from application import app, db
from flask import redirect, render_template, request, url_for
from application.kaapit.models import Kaappi

@app.route("/kaapit", methods=["GET"])
def kaappi_listaus():
    return render_template("kaapit/listaa.html", kaapit = Kaappi.query.all())

@app.route("/kaapit/lisaa/")
def kaappi_lisays():
    return render_template("kaapit/lisaa.html")

@app.route("/kaapit/", methods=["POST"])
def kaappi_lisaaja():
    nimi = request.form.get("nimi")
    tasot = request.form.get("tasot")
    k = Kaappi(nimi, tasot)
    db.session().add(k)
    db.session().commit()
  
    return redirect(url_for("kaappi_listaus"))
