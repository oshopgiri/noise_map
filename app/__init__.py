from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()


def create_app(config_filename=None):
    application = Flask(__name__, instance_relative_config=True, static_url_path='/public')
    application.config.from_pyfile(config_filename)
    application.config["MONGO_URI"] = "mongodb://localhost:27017/niose_app"

    initialize_extensions(application)
    register_blueprints(application)
    return application

def initialize_extensions(application):
    mongo.init_app(application)
    from app.models.user import User

def register_blueprints(application):
    from app.controllers import predict_blueprints
    application.register_blueprint(predict_blueprints)
