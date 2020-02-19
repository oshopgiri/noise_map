from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()


def create_app(config_filename=None):
    application = Flask(__name__, instance_relative_config=True)
    # application.config.from_pyfile(config_filename)
    application.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/codeitup_team10'

    initialize_extensions(application)
    register_blueprints(application)
    return application


def initialize_extensions(application):
    mongo.init_app(application)
    from app.models.location import Location


def register_blueprints(application):
    from app.controllers import predict_blueprints
    application.register_blueprint(predict_blueprints)
