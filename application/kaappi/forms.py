from flask_wtf import FlaskForm
from wtforms import StringField, validators

class KaappiForm(FlaskForm):
    nimi = StringField("Nimi: ", [validators.InputRequired(), validators.Length(min=4, max=16)])

    class Meta:
        csrf = False