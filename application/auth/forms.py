from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    tunnus = StringField("Käyttäjätunnus: ", [validators.InputRequired()])
    salasana = PasswordField("Salasana: ", [validators.InputRequired()])

    class Meta:
        csrf = False


class CreateAccount(FlaskForm):
    tunnus = StringField("Käyttäjätunnus", [validators.InputRequired(), validators.Length(min=4, max=10)])
    salasana = PasswordField('Salasana', [validators.InputRequired(), validators.Length(min=5, max=16),
                                          validators.EqualTo('varmistus', message='Salasanat eivät täsmää!')])
    varmistus = PasswordField('Salasanan uudestaan')

    class Meta:
        csrf = False
