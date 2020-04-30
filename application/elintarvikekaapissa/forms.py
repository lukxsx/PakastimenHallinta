from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField, IntegerField
from wtforms.widgets.html5 import NumberInput

from application.elintarvike.models import Elintarvike
from application.kaappi.models import Kaappi


class EKForm(FlaskForm):
    elintarvike = QuerySelectField('Elintarvike',
                                   query_factory=lambda: Elintarvike.query.filter_by(kayttaja_id=current_user.id).all(),
                                   allow_blank=False, get_label='nimi')
    kaappi = QuerySelectField('Kaappi',
                              query_factory=lambda: Kaappi.query.filter_by(kayttaja_id=current_user.id).all(),
                              allow_blank=False, get_label='nimi')
    taso = IntegerField("Taso", widget=NumberInput(min=1, max=10), default=1)
    maara = IntegerField("Määrä", widget=NumberInput(min=1, max=100), default=1)
    laitettu = DateField('Laitettu kaappiin', [validators.InputRequired()])

    class Meta:
        csrf = False
