from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ElintarvikeForm(FlaskForm):
    nimi = StringField("Nimi: ", [validators.InputRequired()])
    sailyvyys = StringField("Säilyvyys päivinä: ", [validators.InputRequired()])

    class Meta:
        csrf = False