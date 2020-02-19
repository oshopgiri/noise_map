import joblib
import os
import pandas
from sklearn.linear_model import LinearRegression

MODEL_FILE_PATH = '../app/static/model.dat'

if os.path.exists(MODEL_FILE_PATH):
    os.remove(MODEL_FILE_PATH)

dataset = pandas.read_csv('../app/static/output.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

regressor = LinearRegression()
regressor.fit(X, Y)

joblib.dump(regressor, MODEL_FILE_PATH)
