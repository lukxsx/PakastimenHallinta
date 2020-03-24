from application import app, db
from flask import redirect, render_template, request, url_for
from application.elintarvike.models import Elintarvike
from application.elintarvike.forms import ElintarvikeForm


@app.route("/elintarvikkeet", methods=["GET"])
def elintarvike_listaus():
    return render_template("elintarvikkeet/listaa.html", elintarvikkeet=Elintarvike.query.all())


@app.route("/elintarvikkeet/lisaa/")
def elintarvike_lisays():
    return render_template("elintarvikkeet/lisaa.html", form = ElintarvikeForm())


@app.route("/elintarvikkeet/<elintarvike_id>/", methods=["POST"])
def elintarvike_paivitys(elintarvike_id):
    elin = Elintarvike.query.get(elintarvike_id)
    elin.sailyvyys = request.form.get("uusi")
    db.session.commit()
    return redirect(url_for("elintarvike_listaus"))


@app.route("/elintarvikkeet/", methods=["POST"])
def elintarvike_lisaaja():
    form = ElintarvikeForm(request.form)
    if not form.validate():
        return render_template("elintarvike/lisaa.html", form = form)

    e = Elintarvike(form.nimi.data, form.sailyvyys.data)
    db.session().add(e)
    db.session().commit()

    return redirect(url_for("elintarvike_listaus"))
