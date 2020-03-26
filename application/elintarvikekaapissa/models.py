from application import db


class ElintarvikeKaapissa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taso = db.Column(db.Integer, nullable=False)
    maara = db.Column(db.Integer, nullable=False)
    laitettu_kaappiin = db.Column(db.DateTime, default=db.func.current_timestamp())
    elintarvike_id = db.Column(db.Integer, db.ForeignKey('elintarvike.id'), nullable=False)
    kaappi_id = db.Column(db.Integer, db.ForeignKey('kaappi.id'), nullable=False)

    def __init__(self, taso, maara):
        self.taso = taso
        self.maara = maara
