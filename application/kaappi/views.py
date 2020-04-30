from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.kaappi.models import Kaappi
from application.kaappi.forms import KaappiForm, RenameForm
from application.elintarvikekaapissa.models import ElintarvikeKaapissa


@app.route("/kaapit", methods=["GET"])
@login_required
def kaappi_listaus():
    return render_template("kaapit/listaa.html", kaapit=Kaappi.query.filter_by(kayttaja_id=current_user.id).all(),
                           rename=RenameForm())


@app.route("/kaapit/lisaa/")
@login_required
def kaappi_lisays():
    return render_template("kaapit/lisaa.html", form = KaappiForm())


@app.route("/kaapit/", methods=["POST"])
@login_required
def kaappi_lisaaja():
    form = KaappiForm(request.form)
    if not form.validate():
        return render_template("kaapit/lisaa.html", form = form)

    k = Kaappi(form.nimi.data)
    k.kayttaja_id = current_user.id
    db.session().add(k)
    db.session().commit()

    return redirect(url_for("kaappi_listaus"))

@app.route("/kaapit/poista/<kaappi_id>/", methods=["POST"])
@login_required
def kaappi_poisto(kaappi_id):
    kaappi = Kaappi.query.get(kaappi_id)
    ek = ElintarvikeKaapissa.query.filter_by(kaappi_id=kaappi_id).first()
    if ek is None:
        db.session.delete(kaappi)
        db.session.commit()
    else:
        return render_template("error.html", errormessage="VIRHE: Kaappia, jossa on elintarvikkeita ei voi poistaa.")
    return redirect(url_for("kaappi_listaus"))

@app.route("/kaapit/rename/<kaappi_id>/", methods=["POST"])
@login_required
def kaappi_rename(kaappi_id):
    kaappi = Kaappi.query.get(kaappi_id)
    kaappi.nimi = request.form.get("uusi")
    db.session.commit()
    return redirect(url_for("kaappi_listaus"))