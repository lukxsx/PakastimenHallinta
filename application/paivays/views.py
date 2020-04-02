from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
import datetime
from application.elintarvikekaapissa.models import ElintarvikeKaapissa

today = datetime.datetime.now()
print(today)

e = ElintarvikeKaapissa.query.filter_by(id=1).first()
print(e.date_created)

@app.route("/paivays", methods=["GET"])
@login_required
def kaappi_listaus():
    return render_template