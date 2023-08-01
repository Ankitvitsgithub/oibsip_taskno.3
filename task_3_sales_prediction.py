# -*- coding: utf-8 -*-
"""task 3 sales prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fKHzPd0kzs7q7qe7Sp8-jUmiQ2Cz0LpR

Name - Ankit Yadav

Task 3 - Sales Prediction
"""

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

Dataset = pd.read_csv('/content/Advertising.csv')
Dataset

Dataset = Dataset.drop(columns=['Unnamed: 0'], axis=1)
Dataset

Dataset.info()

Dataset.describe()

x = Dataset.iloc[:,:-1].values
y = Dataset.iloc[:,-1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state = 0)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

dt = DecisionTreeRegressor(max_depth = 5)
dt.fit(x_train, y_train)

y_train_pred = dt.predict(x_train)
y_test_pred = dt.predict(x_test)

r2_score(y_train, y_train_pred)*100

r2_score(y_test, y_test_pred)*100

rfc = RandomForestRegressor(max_depth = 5, n_estimators = 1000, min_samples_split = 3)
rfc.fit(x_train, y_train)

y_pred1 = rfc.predict(x_test)

r2_score(y_train, rfc.predict(x_train))*100

r2_score(y_test, y_pred1)*100