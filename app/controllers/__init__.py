import os
from flask import Blueprint

from app.controllers.predict_controller import index as predict_index
from app.controllers.predict_controller import home as predict_home

template_dir = os.path.abspath('app/views/predict')

predict_blueprints = Blueprint('predict', 'api', template_folder=template_dir)
predict_blueprints.add_url_rule('/predict', view_func=predict_index, methods=['GET'])
predict_blueprints.add_url_rule('/', view_func=predict_home, methods=['GET'])
