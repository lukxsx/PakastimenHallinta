from flask import render_template
from application import app
from application.kaappi.models import Kaappi
from flask_login import login_required, current_user

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tilastot")
@login_required
def tilastot():
    return render_template("tilastot.html", kaappisisalto = Kaappi.kaappisisalto(k_id=current_user.id),
                           tyhjat = Kaappi.tyhjatkaapit(k_id=current_user.id))