import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

'''
Jak uruchmiać aplikację :
    
    (venv_car_owners_python_3_11) car-owners-project>flask --app car_owners run --debug

Jak uruchamiać migrację :

    (venv_car_owners_python_3_11) car-owners-project>flask --app car_owners db init

    (venv_car_owners_python_3_11) car-owners-project>flask --app car_owners db migrate -m "Initial migration."

    (venv_car_owners_python_3_11) car-owners-project>flask --app car_owners db upgrade

    (venv_car_owners_python_3_11) car-owners-project>flask --app car_owners db check
'''

# create the extension
db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///car_owners.db'
        # DATABASE=os.path.join(app.instance_path, 'car_owners.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # configure the SQLite database, relative to the app instance folder
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///databases/project.db"
    # initialize the app with the extension
    db.init_app(app)

    # data base changes migration
    migrate.init_app(app, db)

    # blue prints registration
    from blue_prints.bp_owner_api import bp_owner_api
    from blue_prints.bp_vehicle_api import bp_vehicle_api
    app.register_blueprint(bp_owner_api)
    app.register_blueprint(bp_vehicle_api)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Create tables that do not exist in the database. This does not update existing tables, use a migration library for that.
    # This requires that a Flask application context is active.
    with app.app_context():
        db.create_all()

    return app
