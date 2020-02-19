from flask import jsonify, render_template
import joblib
import numpy
from sklearn.linear_model import LinearRegression


def index():
    return render_template('index.html')


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
