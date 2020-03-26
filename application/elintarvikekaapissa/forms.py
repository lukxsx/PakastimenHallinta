from flask_wtf import FlaskForm
from application import db
from application.elintarvike.models import Elintarvike
from application.kaappi.models import Kaappi
from wtforms import StringField, validators, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class EKForm(FlaskForm):
    elintarvike = QuerySelectField('Elintarvike: ', query_factory=lambda: Elintarvike.query, allow_blank=False, get_label='nimi')
    kaappi = QuerySelectField('Kaappi: ', query_factory=lambda : Kaappi.query, allow_blank=False, get_label='nimi')
    taso = StringField('Taso: ', [validators.InputRequired()])
    maara = StringField('Määrä: ', [validators.InputRequired()])
    class Meta:
        csrf = False