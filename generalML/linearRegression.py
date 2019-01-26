# features & labels

import pandas as pd
import quandl
import math

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
df.dropna(inplace=True)



print (df.tail())