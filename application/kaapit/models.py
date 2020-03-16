from application import db

class Kaappi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.String(144), nullable=False)
    tasoja = db.Column(db.Integer, nullable=False)

    def __init__(self, nimi, tasoja):
        self.nimi = nimi
        self.tasoja = tasoja
