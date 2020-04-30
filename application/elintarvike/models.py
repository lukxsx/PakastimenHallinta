from application import db
from application.models import Base

class Elintarvike(Base):
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)
    sailyvyys = db.Column(db.Integer, nullable=False)
    kayttaja_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'), nullable=False)

    elintarvikkeet_kaapissa = db.relationship("ElintarvikeKaapissa", backref='account', lazy=True)

    def __init__(self, nimi, s):
        self.nimi = nimi
        self.sailyvyys = s
