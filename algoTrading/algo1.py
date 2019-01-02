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

# df.plot()
# plot a single statistic
# df['Adj Close'].plot()
plt.show()


