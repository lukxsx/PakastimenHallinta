from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.fields.html5 import IntegerField
from wtforms.widgets.html5 import NumberInput


class ElintarvikeForm(FlaskForm):
    nimi = StringField("Nimi", [validators.InputRequired()])
    sailyvyys = IntegerField("Säilyvyys päivinä", widget=NumberInput(min=1, max=365), default=1)

    class Meta:
        csrf = False


class PaivitysForm(FlaskForm):
    uusi = IntegerField("Uusi säilyvyys", widget=NumberInput(min=1, max=365), default=1)

    class Meta:
        csrf = False
