from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.elintarvike.forms import ElintarvikeForm, PaivitysForm
from application.elintarvike.models import Elintarvike
from application.elintarvikekaapissa.models import ElintarvikeKaapissa


@app.route("/elintarvikkeet", methods=["GET"])
@login_required
def elintarvike_listaus():
    return render_template("elintarvikkeet/listaa.html",
                           elintarvikkeet=Elintarvike.query.filter_by(kayttaja_id=current_user.id).all(),
                           pform=PaivitysForm())


@app.route("/elintarvikkeet/lisaa/")
@login_required
def elintarvike_lisays():
    return render_template("elintarvikkeet/lisaa.html", form=ElintarvikeForm())


@app.route("/elintarvikkeet/<elintarvike_id>/", methods=["POST"])
@login_required
def elintarvike_paivitys(elintarvike_id):
    elin = Elintarvike.query.get(elintarvike_id)
    elin.sailyvyys = request.form.get("uusi")
    db.session.commit()
    return redirect(url_for("elintarvike_listaus"))


@app.route("/elintarvikkeet/poista/<elintarvike_id>/", methods=["POST"])
@login_required
def elintarvike_poisto(elintarvike_id):
    elin = Elintarvike.query.get(elintarvike_id)
    ek = ElintarvikeKaapissa.query.filter_by(elintarvike_id=elintarvike_id).first()
    if ek is None:
        db.session.delete(elin)
        db.session.commit()
    else:
        return render_template("error.html",
                               errormessage="VIRHE: Elintarviketyyppiä, joka on kaapissa ei voida poistaa.")
    return redirect(url_for("elintarvike_listaus"))


@app.route("/elintarvikkeet/", methods=["POST"])
@login_required
def elintarvike_lisaaja():
    form = ElintarvikeForm(request.form)
    if not form.validate():
        return render_template("elintarvikkeet/lisaa.html", form=form)

    e = Elintarvike(form.nimi.data, form.sailyvyys.data)
    e.kayttaja_id = current_user.id
    db.session().add(e)
    db.session().commit()

    return redirect(url_for("elintarvike_listaus"))
