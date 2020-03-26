from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    tunnus = StringField("Käyttäjätunnus: ", [validators.InputRequired()])
    salasana = PasswordField("Salasana: ", [validators.InputRequired()])

    class Meta:
        csrf = False


class CreateAccount(FlaskForm):
    tunnus = StringField("Käyttäjätunnus: ", [validators.InputRequired()])
    salasana = PasswordField('Salasana', [validators.InputRequired(), validators.EqualTo('varmistus', message='Salasanat eivät täsmää!')])
    varmistus = PasswordField('Salasanan uudestaan')

    class Meta:
        csrf = False