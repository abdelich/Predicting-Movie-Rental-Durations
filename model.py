# Import any additional modules and start coding below
# Create a column named "rental_length_days" using the columns "return_date" and "rental_date"
# Create two columns of dummy variables from "special_features", which takes the value of 1 when:
# The value is "Deleted Scenes", storing as a column called "deleted_scenes".
# The value is "Behind the Scenes", storing as a column called "behind_the_scenes".
# Set random_state to 9 whenever you use a function/method involving randomness,
# for example, when doing a test-train split.
# Recommend a model yielding a mean squared error (MSE) less than 3 on the test set
# Save the model you would recommend as a variable named best_model,
# and save its MSE on the test set as best_mse

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import mean_squared_error

from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import GradientBoostingRegressor

df = pd.read_csv('rental_info.csv')
print(df.info())
print(df.head())


df['rental_date'] = pd.to_datetime(df['rental_date'])
df['return_date'] = pd.to_datetime(df['return_date'])
df['rental_length_days'] = (df['return_date'] - df['rental_date']).dt.days

df['deleted_scenes'] = df['special_features'].str.contains('Deleted Scenes').astype(int)
df['behind_the_scenes'] = df['special_features'].str.contains('Behind the Scenes').astype(int)
df = df.drop(['rental_date', 'return_date', 'special_features'], axis=1)
print(df['deleted_scenes'], df['behind_the_scenes'])

scaler = StandardScaler()

y = df['rental_length_days']
X = df.drop('rental_length_days', axis=1)
# X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=9, test_size=0.2)

gb_reg = GradientBoostingRegressor()

print(gb_reg.get_params())

param_grid = {
    'n_estimators': [150, 300],
    'learning_rate': [0.05, 0.1],
    'max_depth': [2, 3],
    'subsample': [0.7, 1.0],
    'min_samples_leaf': [1, 5],
}

cv = KFold(n_splits=5, shuffle=True, random_state=9)
gb_reg_grid = GridSearchCV(
    estimator=gb_reg,
    param_grid=param_grid,
    scoring='neg_mean_squared_error',
    cv=cv,
    n_jobs=-1,
    verbose=1
)

gb_reg_grid.fit(X_train, y_train)
best_model = gb_reg_grid.best_estimator_
best_mse = -gb_reg_grid.best_score_

y_predicted = best_model.predict(X_test)

print(mean_squared_error(y_test, y_predicted))
print(best_mse)