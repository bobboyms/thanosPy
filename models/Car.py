import inspect
from configuracao import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vin = db.Column(db.String(120), unique=False, nullable=False)
    brand = db.Column(db.String(120), unique=False, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(120), unique=False, nullable=False)


    def as_dict(self):
       return {c.name: str(getattr(self, c.name)).strip() for c in self.__table__.columns}
