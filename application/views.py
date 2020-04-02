from flask import render_template
from application import app
from application.kaappi.models import Kaappi

@app.route("/")
def index():
    return render_template("index.html", kaappisisalto = Kaappi.kaappisisalto())
