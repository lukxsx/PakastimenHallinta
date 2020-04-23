from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
import datetime
from datetime import timedelta
from application.elintarvikekaapissa.models import ElintarvikeKaapissa
from application.elintarvike.models import Elintarvike
from application.kaappi.models import Kaappi

class Vanhentunut:
    def __init__(self, ek, pvm, paivia):
        self.ek = ek
        self.pvm = pvm
        self.paivia = paivia

    def tulostaVanhentunutPvm(self):
        return "" + str(self.pvm.day) + "." + str(self.pvm.month) + "." + str(self.pvm.year)

@app.route("/paivays", methods=["GET"])
@login_required
def vanhentuneet():
    today = datetime.date.today()
    ek = ElintarvikeKaapissa.query.all()
    vanhentuneet = []
    for elink in ek:
        s = Elintarvike.query.filter_by(id=elink.elintarvike_id).first()
        laitettu = elink.laitettu_kaappiin
        vanhenee = laitettu + datetime.timedelta(days=s.sailyvyys)
        if vanhenee < today:
            paivia = (today - vanhenee).days
            vanhentunut = Vanhentunut(elink, vanhenee, paivia)
            vanhentuneet.append(vanhentunut)


    return render_template("paivays/listaus.html", lista=vanhentuneet, elin=Elintarvike, kaappi=Kaappi)