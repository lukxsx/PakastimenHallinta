from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
import datetime
from datetime import timedelta
from application.elintarvikekaapissa.models import ElintarvikeKaapissa
from application.elintarvike.models import Elintarvike

@app.route("/paivays", methods=["GET"])
def vanhentuvat():
    today = datetime.datetime.now()
    ek = ElintarvikeKaapissa.query.all()
    vanhentuneet = []
    for elink in ek:
        s = Elintarvike.query.filter_by(id=elink.elintarvike_id).first()
        laitettu = elink.laitettu_kaappiin
        vanhenee = laitettu + datetime.timedelta(days=s.sailyvyys)
        if vanhenee < today:
            vanhentuneet.append(elink)


    return render_template("paivays/listaus.html", lista=vanhentuneet, elin=Elintarvike)