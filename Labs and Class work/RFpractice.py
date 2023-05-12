import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=sns.load_dataset('iris')
print(df.columns)
# Fitting Random Forest Regression to the dataset
# import the regressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# create regressor object
regressor = RandomForestRegressor(n_estimators = 1000, oob_score =True, n_jobs =3,random_state =50,max_features = 6, min_samples_leaf = 5)
y=df['sepal_width'].values
x=df.drop(['sepal_width'], axis=1)
x=pd.get_dummies(x, columns=["species"])
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# fit the regressor with x and y data
regressor.fit(X_train, y_train)

print(regressor.score(X_test, y_test))

# Visualising the Random Forest Regression results

# arrange for creating a range of values
# from min value of x to max
# value of x with a difference of 0.01
# between two consecutive values



