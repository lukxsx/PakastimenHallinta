from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    tunnus = StringField("Käyttäjätunnus: ", [validators.InputRequired()])
    salasana = PasswordField("Salasana: ", [validators.InputRequired()])

    class Meta:
        csrf = False


class CreateAccount(FlaskForm):
    tunnus = StringField("Käyttäjätunnus: ", [validators.InputRequired()])
    salasana = PasswordField('New Password', [validators.InputRequired(), validators.EqualTo('varmistus', message='Salasanat eivät täsmää!')])
    varmistus = PasswordField('Repeat Password')

    class Meta:
        csrf = False