from flask import jsonify, render_template, send_from_directory
import joblib
import numpy
import os
import pathlib
import random
import string
import geojson

from app.helpers.predict_service import format_for_interface, get_current_noise_levels
from app.models.location import Location


def index():
    return render_template('index.html')


def current_state():
    geo_data = format_for_interface(get_current_noise_levels(), Location.list())
    file_name = f"{''.join(random.sample(string.ascii_lowercase, 10))}.geojson"
    file = open(os.path.join('app', 'static', file_name), 'w+')
    file.write(geojson.dumps(geo_data, sort_keys=True))
    file.close()
    return f"static/{file_name}"


def predict():
    location_numbers = list(range(1, 13))
    location_numbers.remove(11)
    inputs = numpy.array(
        list(
            map(
                lambda location_number: [location_number, 2019, 12, 31, 1435],
                location_numbers
            )
        )
    )

    regressor = joblib.load('/static/model.dat')
    predictions = regressor.predict(inputs)
    return jsonify(dict(zip(location_numbers, predictions.T)))
