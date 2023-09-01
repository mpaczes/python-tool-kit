from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response, jsonify, \
    json, abort
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.exc import NoResultFound

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DateTimeField
from wtforms.validators import DataRequired, Email, Optional

from datetime import datetime

from car_owners import db
from models.owner import Owner

'''
Lista punktów końcowych :

    http://127.0.0.1:5000/bp_owner_html/owners/get      - metoda GET HTTP, lista wszystkich właścicieli
'''

bp_owner_html = Blueprint('bp_owner', __name__, url_prefix='/bp_owner_html', template_folder='templates')


class OwnerForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    date_of_birth = DateTimeField('Date of birth', validators=[Optional()])
    submit = SubmitField('Save owner')


@bp_owner_html.route('/owners/get', methods=['GET'])
def user_list():
    owners = db.session.execute(db.select(Owner).order_by(Owner.last_name)).scalars().all()

    return render_template('bp_owner_template/show_all_users.html', owners=owners)


@bp_owner_html.route('/owners/edit/<int:owner_id>', methods=['GET', 'POST'])
def edit_user(owner_id):
    try:
        owner = db.session.execute(db.select(Owner).where(Owner.owner_id == owner_id)).scalars().one()
        owner_form = OwnerForm()
        if request.method == 'GET':
            return render_template('bp_owner_template/edit_owner.html', owner_form=owner_form, owner_id=owner_id,
                                   owner=owner)
        elif request.method == 'POST':
            if owner_form.validate_on_submit():
                owner.first_name = owner_form.first_name.data
                owner.last_name = owner_form.last_name.data
                owner.email = owner_form.email.data
                owner.date_of_birth = owner_form.date_of_birth.data
                db.session.commit()

                flash('Owner has been updated')

                return redirect(url_for('bp_owner.user_list'))
            else:
                flash('Looks like there was an error')

                return render_template('bp_owner_template/edit_owner.html', owner_form=owner_form, owner_id=owner_id,
                                       owner=owner)
    except NoResultFound:
        abort(404, 'A database result was required but none owner was found.')


@bp_owner_html.route('/owners/add', methods=['GET', 'POST'])
def add_user():
    owner_form = OwnerForm()
    if request.method == 'GET':
        return render_template('bp_owner_template/add_owner.html', owner_form=owner_form)
    elif request.method == 'POST':
        if owner_form.validate_on_submit():
            new_owner = Owner()
            new_owner.first_name = owner_form.first_name.data
            new_owner.last_name = owner_form.last_name.data
            new_owner.email = owner_form.email.data
            new_owner.date_of_birth = owner_form.date_of_birth.data
            db.session.add(new_owner)
            db.session.commit()

            flash('Owner has been created')

            return redirect(url_for('bp_owner.user_list'))
        else:
            flash('Looks like there was an error')

            return render_template('bp_owner_template/add_owner.html', owner_form=owner_form)


@bp_owner_html.route('/owners/delete', methods=['GET'])
def delete_user():
    try:
        owner_id = request.args.get('owner_id')
        owner = db.session.execute(db.select(Owner).where(Owner.owner_id == owner_id)).scalars().one()
        db.session.delete(owner)
        db.session.commit()
        flash('Owner has been deleted')
        return redirect(url_for('bp_owner.user_list'))
    except NoResultFound:
        abort(404, 'A database result was required but none owner was found.')
