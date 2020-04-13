from application import db
from application.models import Base
from sqlalchemy.sql import text

class Kaappi(Base):
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)

    db.relationship("ElintarvikeKaapissa", backref='account', lazy=True)

    def __init__(self, nimi):
        self.nimi = nimi

    @staticmethod
    def kaappisisalto():
        kysely = text("SELECT kaappi.nimi, SUM(elintarvike_kaapissa.maara)"
                      " FROM elintarvike_kaapissa"
                      " LEFT JOIN kaappi ON elintarvike_kaapissa.kaappi_id=kaappi.id"
                      " GROUP BY kaappi.nimi")
        tulos = db.engine.execute(kysely)

        listaus = []
        for rivi in tulos:
            listaus.append({"kaappi": rivi[0], "el": rivi[1]})

        return listaus