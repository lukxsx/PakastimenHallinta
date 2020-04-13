from flask_wtf import FlaskForm
from wtforms import StringField, validators

class KaappiForm(FlaskForm):
    nimi = StringField("Nimi: ", [validators.InputRequired()])

    class Meta:
        csrf = False