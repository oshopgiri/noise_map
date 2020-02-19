from flask import Flask


def create_app(config_filename=None):
    application = Flask(__name__, instance_relative_config=True, static_url_path='/public')
    application.config.from_pyfile(config_filename)

    register_blueprints(application)
    return application


def register_blueprints(application):
    from app.controllers import predict_blueprints
    application.register_blueprint(predict_blueprints)
