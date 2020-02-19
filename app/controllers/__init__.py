import os
from flask import Blueprint

from app.controllers.predict_controller import index as predict_index
from app.controllers.predict_controller import predict as predict_predict
from app.controllers.predict_controller import current_state as predict_current_state

template_dir = os.path.abspath('app/views/predict')

predict_blueprints = Blueprint('predict', 'api', template_folder=template_dir)
predict_blueprints.add_url_rule('/', view_func=predict_index, methods=['GET'])
predict_blueprints.add_url_rule('/current_state', view_func=predict_current_state, methods=['GET'])
predict_blueprints.add_url_rule('/predict', view_func=predict_predict, methods=['POST'])
