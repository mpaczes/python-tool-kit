from car_owners import db


class Owner(db.Model):
    '''Strona jeden ralacji właścicel-pojazd'''
    owner_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)
    date_of_birth = db.Column(db.DateTime, nullable=True)
    vehicles = db.relationship('Vehicle', backref='owner', lazy=True)

    # def __repr__(self):
    #     return '<Owner %r>' % self.first_name + ', ' + self.last_name + ' (' + self.email + ')'


class Vehicle(db.Model):
    '''Strona wiele ralacji właścicel-pojazd'''
    vehicle_id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    date_of_build = db.Column(db.DateTime, nullable=True)
    vin_number = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.owner_id'), nullable=False)
