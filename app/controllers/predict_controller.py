from flask import jsonify, render_template
import geojson
import joblib
import numpy
import os
import random
import string

from app.helpers.predict_service import format_to_geojson, get_current_noise_levels


def index():
    return render_template('index.html')


def current_state():
    geo_data = format_to_geojson(get_current_noise_levels())
    file_name = f"{''.join(random.sample(string.ascii_lowercase, 16))}.geojson"
    with open(os.path.join('app', 'static', 'geojsons', file_name), 'w') as file:
        geojson.dump(geo_data, file, indent=4, sort_keys=True)
    return os.path.join('static', 'geojsons', file_name)


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
