import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import requests
import json

df = pd.read_csv('./data/data.csv')
X = df.iloc[:, :-1].values
print(X)
y = df.iloc[:, 1].values
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

pickle.dump(regressor, open('./data/model.pkl', 'wb'))

# model = pickle.load( open('./data/model.pkl','rb'))
# print(model.predict([[1.8]]))