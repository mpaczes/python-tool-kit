from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response, jsonify, \
    json, abort
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.exc import NoResultFound

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DateTimeField, SelectField
from wtforms.validators import DataRequired, Email, Optional

from datetime import datetime

from car_owners import db
from models.vehicle import Vehicle
from models.owner import Owner

bp_vehicle_html = Blueprint('bp_vehicle', __name__, url_prefix='/bp_vehicle_html', template_folder='templates')


class VehicleForm(FlaskForm):
    vin_number = StringField('VIN  number', validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    date_of_build = DateTimeField('Date of build', validators=[Optional()])
    owners = SelectField('Owners', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Save vehicle')


@bp_vehicle_html.route('/vehicles/add_vehicle', methods=['GET', 'POST'])
def add_vehicle():
    vehicle_form = VehicleForm()
    owners = db.session.execute(db.select(Owner).order_by(Owner.last_name)).scalars().all()
    vehicle_form.owners.choices = [(owner.owner_id, owner.first_name + ' ' + owner.last_name) for owner in owners]
    if request.method == 'GET':
        return render_template('bp_vehicle_template/add_vehicle.html', vehicle_form=vehicle_form)
    elif request.method == 'POST':
        if vehicle_form.validate_on_submit():
            new_vehicle = Vehicle()

            new_vehicle.vin_number = vehicle_form.vin_number.data
            new_vehicle.brand = vehicle_form.brand.data
            new_vehicle.model = vehicle_form.model.data
            new_vehicle.color = vehicle_form.color.data
            new_vehicle.date_of_build = vehicle_form.date_of_build.data
            new_vehicle.owner_id = vehicle_form.owners.data

            db.session.add(new_vehicle)
            db.session.commit()

            flash('Vehicle has been created')
            return redirect(url_for('bp_vehicle.vehicle_list'))
        else:
            flash('Looks like there was an error')

            return render_template('bp_vehicle_template/add_vehicle.html', vehicle_form=vehicle_form)


@bp_vehicle_html.route('/vehicles/get', methods=['GET'])
def vehicle_list():
    vehicles = db.session.execute(db.select(Vehicle).order_by(Vehicle.brand, Vehicle.model)).scalars().all()

    return render_template('bp_vehicle_template/show_all_vehicles.html', vehicles=vehicles)
