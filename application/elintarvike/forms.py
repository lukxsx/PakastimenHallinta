from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField

class ElintarvikeForm(FlaskForm):
    nimi = StringField("Nimi", [validators.InputRequired()])
    sailyvyys = IntegerField("Säilyvyys päivinä", [validators.InputRequired(),
                                                    validators.NumberRange(min=1, max=365, message="Anna kelvollinen säilyvyysaika"),
                                                    validators.Optional(strip_whitespace=True)])

    class Meta:
        csrf = False