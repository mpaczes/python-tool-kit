from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response, jsonify, \
    json, abort
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.exc import NoResultFound

from datetime import datetime

from car_owners import db
from models.owner import Owner

'''
Lista punktów końcowych :

    http://127.0.0.1:5000/bp_owner_html/owners      - metoda GET HTTP, lista wszystkich właścicieli
'''

bp_owner_html = Blueprint('bp_owner', __name__, url_prefix='/bp_owner_html', template_folder='templates')


@bp_owner_html.route('/owners', methods=['GET'])
def user_list():
    owners = db.session.execute(db.select(Owner).order_by(Owner.last_name)).scalars().all()

    return render_template('bp_owner_template/show_all_users.html', owners=owners)
