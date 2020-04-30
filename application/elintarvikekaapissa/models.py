from application import db
from application.models import Base


class ElintarvikeKaapissa(Base):
    id = db.Column(db.Integer, primary_key=True)
    taso = db.Column(db.Integer, nullable=False)
    maara = db.Column(db.Integer, nullable=False)
    laitettu_kaappiin = db.Column(db.Date, default=db.func.current_timestamp())
    elintarvike_id = db.Column(db.Integer, db.ForeignKey('elintarvike.id'), nullable=False)
    kaappi_id = db.Column(db.Integer, db.ForeignKey('kaappi.id'), nullable=False)
    kayttaja_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'), nullable=False)

    def __init__(self, elintarvike_id, kaappi_id, taso, maara, laitettu):
        self.taso = taso
        self.maara = maara
        self.elintarvike_id = elintarvike_id
        self.kaappi_id = kaappi_id
        self.laitettu_kaappiin = laitettu
