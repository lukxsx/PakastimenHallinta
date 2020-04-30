from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tietokanta.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# pääsivut
from application import views

# elintarvikkeet
from application.elintarvike import models, views

# elintarvikkeet kaapissa
from application.elintarvikekaapissa import models, views

# kaapit
from application.kaappi import models, views

# paivays
from application.paivays import views

# kirjautuminen
from application.auth import models, views
from application.auth.models import Kayttaja
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "kirjautuminen"
login_manager.login_message = "Kirjaudu sisään"

@login_manager.user_loader
def load_user(user_id):
    return Kayttaja.query.get(user_id)

try:
    db.create_all()
except:
    pass