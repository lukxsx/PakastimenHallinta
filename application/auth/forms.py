from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField

class LoginForm(FlaskForm):
    tunnus = StringField("Käyttäjätunnus: ")
    salasana = PasswordField("Salasana: ")

    class Meta:
        csrf = False