from application import db


class Elintarvike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)
    sailyvyys = db.Column(db.Integer, nullable=False)

    def __init__(self, nimi, s):
        self.nimi = nimi
        self.sailyvyys = s
