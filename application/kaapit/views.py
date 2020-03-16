from application import app, db
from flask import render_template, request
from application.kaapit.models import Kaappi

@app.route("/kaapit/lisaa/")
def kaappi_kysely():
    return render_template("kaapit/lisaa.html")

@app.route("/kaapit/", methods=["POST"])
def kaappi_lisays():
    nimi = request.form.get("nimi")
    tasot = request.form.get("tasot")
    k = Kaappi(nimi, tasot)
    db.session().add(k)
    db.session().commit()
  
    return "hello world!"
