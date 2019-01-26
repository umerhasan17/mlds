# features & labels

import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

df = quandl.get('WIKI/GOOGL')

# useless features can cause a lot of problems for machine learning classifiers
# take only important features

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# arthur samuel ML in the 50s

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df ['Adj. Close'] * 100
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df ['Adj. Open'] * 100

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
# we don't want to get rid of all the data, so we treat it as an outlier
# pandas doesn't allow any empty columns
df.fillna('-99999', inplace=True)

forecast_out = int(math.ceil(0.01 * len(df)))

# creating the label
df['label'] = df[forecast_col].shift(-forecast_out)

# all our features is everything but label
X = np.array(df.drop(['label'], 1))

# skip in HFT
X = preprocessing.scale(X)

X = X[:-forecast_out]
# the X values we don't have y values for
X_lately = X[-forecast_out:]

df.dropna(inplace=True)
y = np.array(df['label'])

# splitting up train and test
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
# clf = svm.SVR(kernel='poly')
# 97 with linear regression
# 78 with linear svm
# 60 with polynomial svm
# not really sure why
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
# 97% accuracy

forecast_set = clf.predict(X_lately)

print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan, for _ in range(len(df.columns) - 1)] + [i]

df['Adj. Close'].plot()
df['Forcast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()