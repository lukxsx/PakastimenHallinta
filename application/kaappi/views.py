from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.kaappi.models import Kaappi
from application.kaappi.forms import KaappiForm


@app.route("/kaapit", methods=["GET"])
@login_required
def kaappi_listaus():
    return render_template("kaapit/listaa.html", kaapit=Kaappi.query.all())


@app.route("/kaapit/lisaa/")
@login_required
def kaappi_lisays():
    return render_template("kaapit/lisaa.html", form = KaappiForm())


@app.route("/kaapit/<kaappi_id>/", methods=["POST"])
@login_required
def kaappi_paivitys(kaappi_id):
    k = Kaappi.query.get(kaappi_id)
    k.tasoja = request.form.get("uusi")
    db.session.commit()
    return redirect(url_for("kaappi_listaus"))


@app.route("/kaapit/", methods=["POST"])
@login_required
def kaappi_lisaaja():
    form = KaappiForm(request.form)
    if not form.validate():
        return render_template("kaapit/lisaa.html", form = form)

    k = Kaappi(form.nimi.data, form.tasoja.data)
    db.session().add(k)
    db.session().commit()

    return redirect(url_for("kaappi_listaus"))
