from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response, jsonify, json
from werkzeug.security import check_password_hash, generate_password_hash

from datetime import date

from car_owners import db
from models.owner import Owner

'''
URL'e do testowania API :

    curl -X GET http://localhost:5000/bp_owner_api/owners
    
    curl -X GET http://localhost:5000/bp_owner_api/owners/3

    curl -X POST http://localhost:5000/bp_owner_api/owners -H "Content-type: application/json" -d "{\"first_name\":\"marcelina\",\"last_name\":\"zawadzka\",\"email\":\"marcelin.zawadzka@tlen.cz\"}"

    curl -X DELETE http://localhost:5000/bp_owner_api/owners/3

    curl -X PUT http://localhost:5000/bp_owner_api/owners/3 -H "Content-type: application/json" -d "{\"first_name\":\"Arnold\"}"
'''

bp_owner_api = Blueprint('owner_api', __name__, url_prefix='/bp_owner_api')


@bp_owner_api.route('/owners', methods=['GET'])
def user_list():
    owners = db.session.execute(db.select(Owner).order_by(Owner.last_name)).scalars().all()

    owners_as_dict = list()
    for owner in owners:
        temp_dict = dict()
        temp_dict['owner_id'] = owner.owner_id
        temp_dict['first_name'] = owner.first_name
        temp_dict['last_name'] = owner.last_name
        temp_dict['date_of_birth'] = owner.date_of_birth
        temp_dict['email'] = owner.email

        owners_as_dict.append(temp_dict)

    return make_response(owners_as_dict, 200)


@bp_owner_api.route('/owners/<int:owner_id>', methods=['GET'])
def user_single(owner_id):
    owner = db.session.execute(db.select(Owner).where(Owner.owner_id == owner_id)).scalars().one()

    owner_as_dict = dict()
    owner_as_dict['owner_id'] = owner.owner_id
    owner_as_dict['first_name'] = owner.first_name
    owner_as_dict['last_name'] = owner.last_name
    owner_as_dict['date_of_birth'] = owner.date_of_birth
    owner_as_dict['email'] = owner.email

    return make_response(owner_as_dict, 200)


@bp_owner_api.route("/owners", methods=['POST'])
def user_create():
    # content_type = request.headers.get('Content-Type')
    if request.is_json:
        data = request.json
        print('Request is json')
    else:
        data = json.loads(request.data)
        print('Request is not json')

    first_name = data.get('first_name', None)
    last_name = data.get('last_name', None)
    email = data.get('email', None)

    owner = Owner(first_name=first_name, last_name=last_name, email=email)
    db.session.add(owner)
    db.session.commit()

    return make_response('Owner has been created', 200)


@bp_owner_api.route("/owners/<int:owner_id>", methods=['DELETE'])
def user_delete(owner_id):
    owner = db.session.execute(db.select(Owner).where(Owner.owner_id == owner_id)).scalars().one()

    db.session.delete(owner)
    db.session.commit()

    return make_response('Owner has been deleted', 200)


@bp_owner_api.route("/owners/<int:owner_id>", methods=['PUT'])
def user_update(owner_id):
    owner = db.session.execute(db.select(Owner).where(Owner.owner_id == owner_id)).scalars().one()

    if request.is_json:
        data = request.json
        print('Request is json')
    else:
        data = json.loads(request.data)
        print('Request is not json')

    first_name = data.get('first_name', None)
    last_name = data.get('last_name', None)
    email = data.get('email', None)

    if first_name:
        owner.first_name = first_name
    if last_name:
        owner.last_name = last_name
    if email:
        owner.email = email

    db.session.commit()

    return make_response('Owner has been updated', 200)
