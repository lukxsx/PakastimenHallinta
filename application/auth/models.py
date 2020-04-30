from application import db
from application.models import Base


class Kayttaja(Base):
    __tablename__ = "kayttaja"

    id = db.Column(db.Integer, primary_key=True)
    tunnus = db.Column(db.String(144), nullable=False)
    salasana = db.Column(db.String(144), nullable=False)

    kaapit = db.relationship("Kaappi", backref='kayttaja', lazy=True)

    def __init__(self, tunnus, salasana):
        self.tunnus = tunnus
        self.salasana = salasana

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
