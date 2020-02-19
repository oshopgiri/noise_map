import joblib
import numpy
from sklearn.linear_model import LinearRegression

MODEL_FILE_NAME = 'model.dat'

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

print(inputs)

regressor = joblib.load(MODEL_FILE_NAME)
predictions = regressor.predict(inputs)
print(predictions)
