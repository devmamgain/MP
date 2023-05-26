# -*- coding: utf-8 -*-
"""Mielage Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15zIa-s3MFKGE8y3BRe7L_ZHzMUHRASU_

# **Mileage Prediction - Regression Analysis**

**Source:**

This dataset was taken from the StatLib library which is maintained at Carnegie Mellon University.The dataset was used in 1983 American Statiscal Association Exposition.

**Objective:**

The data concerns city-cycle fuel consumption in miles per gallon, to be predicted in terms of 3 multivalued discrete and 5 continuous attributes

# **Import Library**
"""

import pandas as pd
import numpy as nm
import matplotlib.pyplot as pl
import seaborn as sea

"""# **Import Data**"""

ml = pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/MPG.csv')

ml.head()

ml.nunique()

"""# **Data PreProcessing**"""

ml.info()

ml.describe()

ml.corr()

"""# **Remove Missing Values**"""

ml = ml.dropna()

ml.info()

"""# **Data Visualization**"""

sea.pairplot(ml, x_vars= ['displacement','horsepower','weight','acceleration','mpg'], y_vars=['mpg']);

sea.regplot(x='displacement',y='mpg',data=ml);

"""# **Define Target Variable y and Feature x**"""

ml.columns

y=ml['mpg']

y.shape

x=ml[['displacement','horsepower','weight','acceleration']]

x.shape

x

"""# **Scaling Data**"""

from sklearn.preprocessing import StandardScaler

ss=StandardScaler()

x=ss.fit_transform(x)

x

pd.DataFrame(x).describe()

"""# **Train Test Split Data**"""

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y, train_size=0.7,random_state = 2529)

x_train.shape, x_test.shape, y_train.shape, y_test.shape

"""# **Linear Regression Model**"""

from sklearn.linear_model import LinearRegression

l=LinearRegression()

l.fit(x_train,y_train)

l.intercept_

l.coef_

"""# **Predict Test Data**"""

y_pred=l.predict(x_test)

y_pred

"""# **Model Accuracy**"""

from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, r2_score

mean_absolute_error(y_test, y_pred)

mean_absolute_percentage_error(y_test,y_pred)

r2_score(y_test,y_pred)

"""# **Polynomial Regression**"""

from sklearn.preprocessing import PolynomialFeatures

p = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)

x_train2 = p.fit_transform(x_train)

x_test2 = p.fit_transform(x_test)

l.fit(x_train2, y_train)

l.intercept_

l.coef_

y_pred_p = l.predict(x_test2)

"""# **Model Accuracy**"""

from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, r2_score

mean_absolute_error(y_test, y_pred_p)

mean_absolute_percentage_error(y_test, y_pred_p)

r2_score(y_test, y_pred_p)