import joblib
import pandas
from sklearn.linear_model import LinearRegression

MODEL_FILE_NAME = 'model.dat'

dataset = pandas.read_csv('output.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

regressor = LinearRegression()
regressor.fit(X, Y)

joblib.dump(regressor, MODEL_FILE_NAME)
