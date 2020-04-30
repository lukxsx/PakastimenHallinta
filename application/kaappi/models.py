from application import db
from application.models import Base
from sqlalchemy.sql import text

class Kaappi(Base):
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)
    kayttaja_id = db.Column(db.Integer, db.ForeignKey('kayttaja.id'), nullable=False)

    db.relationship("ElintarvikeKaapissa", backref='account', lazy=True)

    def __init__(self, nimi):
        self.nimi = nimi

    @staticmethod
    def kaappisisalto(k_id):
        kysely = text("SELECT kaappi.nimi, SUM(elintarvike_kaapissa.maara)"
                      " FROM elintarvike_kaapissa"
                      " LEFT JOIN kaappi ON elintarvike_kaapissa.kaappi_id=kaappi.id"
                      " WHERE kaappi.kayttaja_id = :x"
                      " GROUP BY kaappi.nimi").params(x=k_id)
        tulos = db.engine.execute(kysely)

        listaus = []
        for rivi in tulos:
            listaus.append({"kaappi": rivi[0], "el": rivi[1]})

        return listaus

    @staticmethod
    def tyhjatkaapit(k_id):
        kysely = text("SELECT COUNT(id) FROM kaappi WHERE id NOT IN (SELECT kaappi_id FROM elintarvike_kaapissa)"
                      " AND kaappi.kayttaja_id = :x").params(x=k_id)
        tulos = db.engine.execute(kysely)

        listaus = []
        for rivi in tulos:
            listaus.append(rivi[0])

        return listaus[0]