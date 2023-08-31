from car_owners import db


# class Vehicle(db.Model):
#     '''Strona wiele ralacji właścicel-pojazd'''
#     vehicle_id = db.Column(db.Integer, primary_key=True)
#     brand = db.Column(db.String, nullable=False)
#     model = db.Column(db.String, nullable=False)
#     color = db.Column(db.String, nullable=False)
#     date_of_build = db.Column(db.DateTime, nullable=True)
#     vin_number = db.Column(db.DateTime, nullable=False)
#     owner_id = db.Column(db.Integer, db.ForeignKey('owner.owner_id'), nullable=False)

    # def __repr__(self):
    #     return '<Vehicle %r>' % self.brand + ', ' + self.model + ' (' + self.vin_number + ')'
