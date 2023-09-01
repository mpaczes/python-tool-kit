from car_owners import db
from models.vehicle import Vehicle


class Owner(db.Model):
    '''Strona jeden ralacji właścicel-pojazd'''
    owner_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)
    date_of_birth = db.Column(db.DateTime, nullable=True)
    vehicles = db.relationship(Vehicle, backref='owner', lazy=True)
