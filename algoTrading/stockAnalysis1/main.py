# import urllib2
import time
import pandas as pd
# import pandas_datareader.data as web
import datetime

stockToPull = 'AAPL'

def pullData2(stock):
    start = datetime.datetime(2010,1,1)
    end = datetime.datetime(2019,1,1)
    data = pd_datareader.data.DataReader(stock, yahoo, start, end)
    return data


# def pullData(stock):
#     try:
#         fileLine = stock+'.txt'
#         urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1y/csv'
#         sourceCode = urllib2.urlopen(urlToVisit).read()
#         splitSource = sourceCode.split('\n')

#         for eachLine in splitSource:
#             splitLine = eachLine.split(',')


#     except Exception, e:
#         print 'main loop', str(e)

print(pullData2("AAPL"))