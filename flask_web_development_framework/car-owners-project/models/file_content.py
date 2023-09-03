from car_owners import db
from datetime import datetime


class FileContent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, nullable=False)
    file_name = db.Column(db.String(128), nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)        # Actual data, needed for Download
    additional_text = db.Column(db.Text, nullable=True)
    creation_date = db.Column(db.DateTime, nullable=False)
