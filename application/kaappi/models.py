from application import db
from application.models import Base


class Kaappi(Base):
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)
    tasoja = db.Column(db.Integer, nullable=False)

    db.relationship("ElintarvikeKaapissa", backref='account', lazy=True)

    def __init__(self, nimi, t):
        self.nimi = nimi
        self.tasoja = t
