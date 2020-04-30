from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.elintarvike.models import Elintarvike
from application.kaappi.models import Kaappi
from application.elintarvikekaapissa.models import ElintarvikeKaapissa
from application.elintarvikekaapissa.forms import EKForm

@app.route("/ek/lisaa/")
@login_required
def ek_lisays():
    return render_template("elintarvikekaapissa/lisaa.html", form = EKForm())

@app.route("/ek/", methods=["POST"])
@login_required
def ek_lisaaja():
    form = EKForm(request.form)
    if not form.validate():
        return render_template("elintarvikekaapissa/lisaa.html", form = form)
    
    e = form.elintarvike.data.id
    k = form.kaappi.data.id
    taso = form.taso.data
    maara = form.maara.data
    laitettu = form.laitettu.data
    
    ek = ElintarvikeKaapissa(e, k, taso, maara, laitettu)
    ek.kayttaja_id = current_user.id
    db.session.add(ek)
    db.session.commit()

    return redirect(url_for("ek_listaus"))

@app.route("/ek/poista/<ek_id>/", methods=["POST"])
@login_required
def ek_poistaja(ek_id):
    poistettava = ElintarvikeKaapissa.query.get(ek_id)
    db.session.delete(poistettava)
    db.session.commit()
    return redirect(url_for("ek_listaus"))


@app.route("/ek/", methods=["GET"])
@login_required
def ek_listaus():
    return render_template("elintarvikekaapissa/listaa.html",
                           ek=ElintarvikeKaapissa.query.filter_by(kayttaja_id=current_user.id).all(),
                           elin=Elintarvike, kaap=Kaappi)