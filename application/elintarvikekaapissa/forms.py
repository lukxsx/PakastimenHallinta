from flask_wtf import FlaskForm
from application import db
from application.elintarvike.models import Elintarvike
from application.kaappi.models import Kaappi
from wtforms import StringField, validators, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField

class EKForm(FlaskForm):
    elintarvike = QuerySelectField('Elintarvike: ', query_factory=lambda: Elintarvike.query, allow_blank=False, get_label='nimi')
    kaappi = QuerySelectField('Kaappi: ', query_factory=lambda : Kaappi.query, allow_blank=False, get_label='nimi')
    taso = IntegerField('Taso: ', [validators.InputRequired(), validators.NumberRange(min=1, max=10, message="Anna kelvollinen määrä")])
    maara = IntegerField('Määrä: ', [validators.InputRequired(), validators.Optional(strip_whitespace=True),
                                    validators.NumberRange(min=1, max=100, message="Anna kelvollinen määrä")])
    laitettu = DateField('Laitettu kaappiin: ', [validators.InputRequired()])
    class Meta:
        csrf = False