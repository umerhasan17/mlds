import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2019, 1, 1)

# INPUT/OUTPUT

# getting data from online
# df = web.DataReader('TSLA', 'yahoo', start, end) 

# storing data in a csv
# df.to_csv('tsla.csv') 

# getting data from local csv
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0) # getting

# print first 5
# print(df.head()) 
# print last 5
# print(df.tail())

# GRAPHING

# plot the dataframe
# df.plot()
# plot a single statistic
# df['Adj Close'].plot()
# plt.show() to show when running off command line
# plt.show()

# DATA MANIPULATION 100ma

# 100 ma for stock
df['100ma'] = df['Adj Close'].rolling(window=100).mean()
# drop NaNs for the first 100 days of range
df.dropna(inplace=True)

# 2 sub graphs one displaying 2 lines on 1 graph with vol below it
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex = ax1)
ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()
