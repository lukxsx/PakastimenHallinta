from flask_wtf import FlaskForm
from application import db
from application.elintarvike.models import Elintarvike
from application.kaappi.models import Kaappi
from wtforms import validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField, IntegerField
from wtforms.widgets.html5 import NumberInput


class EKForm(FlaskForm):
    elintarvike = QuerySelectField('Elintarvike', query_factory=lambda: Elintarvike.query, allow_blank=False, get_label='nimi')
    kaappi = QuerySelectField('Kaappi', query_factory=lambda : Kaappi.query, allow_blank=False, get_label='nimi')
    taso = IntegerField("Taso", widget=NumberInput(min=1, max=10), default=1)
    maara = IntegerField("Määrä", widget=NumberInput(min=1, max=100), default=1)
    laitettu = DateField('Laitettu kaappiin', [validators.InputRequired()])
    class Meta:
        csrf = False