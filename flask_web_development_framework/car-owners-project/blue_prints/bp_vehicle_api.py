from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response, jsonify, json, abort
from sqlalchemy.exc import NoResultFound
from werkzeug.security import check_password_hash, generate_password_hash

from datetime import datetime

from car_owners import db
from models.vehicle import Vehicle

'''
URL'e do testowania API :

    curl -X GET http://localhost:5000/bp_vehicle_api/vehicles
    
    curl -X GET http://localhost:5000/bp_vehicle_api/vehicles/vin_number/WP0AA2A79BL017244
    
    curl -X POST http://localhost:5000/bp_vehicle_api/vehicles/3 -H "Content-type: application/json" -d "{\"vin_number\":\"JHMSZ542XDC028494\", \"brand\":\"Honda\", \"model\":\"Accord\", \"color\":\"blue\"}"

    curl -X DELETE http://localhost:5000/bp_vehicle_api/vehicles/5
    
    curl -X PUT http://localhost:5000/bp_vehicle_api/vehicles/5 -H "Content-type: application/json" -d "{\"color\":\"gold\"}"

Strona do generowania testowych numerów VIN dla pojazdów :

    https://vingenerator.org/
'''

bp_vehicle_api = Blueprint('vehicle_api', __name__, url_prefix='/bp_vehicle_api')


@bp_vehicle_api.route('/vehicles', methods=['GET'])
def vehicle_list():
    vehicles = db.session.execute(db.select(Vehicle).order_by(Vehicle.brand, Vehicle.model)).scalars().all()

    vehicles_as_dict = list()
    for vehicle in vehicles:
        temp_dict = dict()
        temp_dict['vehicle_id'] = vehicle.vehicle_id
        temp_dict['vin_number'] = vehicle.vin_number
        temp_dict['brand'] = vehicle.brand
        temp_dict['model'] = vehicle.model
        temp_dict['color'] = vehicle.color
        temp_dict['date_of_build'] = vehicle.date_of_build
        temp_dict['owner_id'] = vehicle.owner_id

        vehicles_as_dict.append(temp_dict)

    return make_response(vehicles_as_dict, 200)


@bp_vehicle_api.route('/vehicles/vin_number/<string:vin_number>', methods=['GET'])
def vehicle_single_by_vin_number(vin_number):
    try:
        vehicle = db.session.execute(db.select(Vehicle).where(Vehicle.vin_number == vin_number)).scalars().one()

        vehicle_as_dict = dict()
        vehicle_as_dict['vehicle_id'] = vehicle.vehicle_id
        vehicle_as_dict['vin_number'] = vehicle.vin_number
        vehicle_as_dict['owner_id'] = vehicle.owner_id
        vehicle_as_dict['brand'] = vehicle.brand
        vehicle_as_dict['model'] = vehicle.model
        vehicle_as_dict['color'] = vehicle.color
        vehicle_as_dict['date_of_build'] = vehicle.date_of_build

        return make_response(vehicle_as_dict, 200)
    except NoResultFound:
        abort(404, 'A database result was required but none vehicle was found.')


@bp_vehicle_api.route("/vehicles/<int:owner_id>", methods=['POST'])
def vehicle_create(owner_id):
    if request.is_json:
        data = request.json
    else:
        data = json.loads(request.data)

    vin_number = data.get('vin_number', None)
    brand = data.get('brand', None)
    model = data.get('model', None)
    color = data.get('color', None)
    date_of_build = data.get('date_of_build', None)     # '1990-01-17'
    formatted_date_of_build = None
    if date_of_build:
        formatted_date_of_build = datetime.strptime(date_of_build, '%Y-%m-%d')

    vehicle = Vehicle(owner_id=owner_id, vin_number=vin_number, brand=brand, model= model, color=color,
                      date_of_build=formatted_date_of_build)

    db.session.add(vehicle)
    db.session.commit()

    return make_response('Vehicle has been created', 200)


@bp_vehicle_api.route("/vehicles/<int:vehicle_id>", methods=['DELETE'])
def vehicle_delete(vehicle_id):
    try:
        vehicle = db.session.execute(db.select(Vehicle).where(Vehicle.vehicle_id == vehicle_id)).scalars().one()

        db.session.delete(vehicle)
        db.session.commit()

        return make_response('Vehicle has been deleted', 200)
    except NoResultFound:
        abort(404, 'A database result was required but none vehicle was found.')


@bp_vehicle_api.route("/vehicles/<int:vehicle_id>", methods=['PUT'])
def user_update(vehicle_id):
    try:
        vehicle = db.session.execute(db.select(Vehicle).where(Vehicle.vehicle_id == vehicle_id)).scalars().one()

        if request.is_json:
            data = request.json
        else:
            data = json.loads(request.data)

        vin_number = data.get('vin_number', None)
        color = data.get('color', None)
        owner_id = data.get('owner_id', None)
        if vin_number:
            vehicle.vin_number = vin_number
        if color:
            vehicle.color = color
        if owner_id:
            vehicle.owner_id = owner_id

        db.session.commit()

        return make_response('Vehicle has been updated', 200)
    except NoResultFound:
        abort(404, 'A database result was required but none vehicle was found.')
