import pandas as pd
import pandas_datareader.data as web
import pickle
import datetime as dt
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter
from sklearn import svm, model_selection, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier

style.use('ggplot')

# creating compiled csv of all Adj Close stocks
def compile_data():
    with open ("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)
    
    main_df = pd.DataFrame()

    for count, ticker in enumerate(tickers):
        try:
            df = pd.read_csv('stock_dfs/{}.csv'.format(ticker))
        except:
            break
        df.set_index('Date', inplace=True)
        df.rename(columns= {'Adj Close': ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer')
        
        if count % 10 == 0:
            print(count)
    
    print(main_df.head())
    main_df.to_csv('sp500_joined_closes.csv')

# this function creates the correlation heatmap
def visualize_data():
    df = pd.read_csv('sp500_joined_closes.csv')
    df_corr = df.corr()
    print(df_corr.head())

    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)

    fig.colorbar(heatmap)

    # arranging ticks at every half mark 
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    # our correlation range 
    heatmap.set_clim(-1,1)
    plt.tight_layout()
    plt.show()

# generally companies move together as shown by the heatmap. 
# however they may lag behind each other. 
# this function tries to identify the lag. 
# the time scale should be 1 / 2 years for this strategy as company relations change overtime. 
def process_data_for_labels(ticker):
    # the time tange we are working with
    hm_days = 7
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days+1):
        # get the value for the stock a specific number of days in the future
        # -i to get future data
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)

    return tickers, df

# features - percent change 
# labels - buy, sell, hold
def buy_sell_hold(*args):
    # passing in whole week of percent changes
    cols = [c for c in args]
    # if stock price changes more than 2 percent in a week (buy/sell)
    requirement = 0.028

    for col in cols:
        if col > requirement:
            return 1
        if col < -requirement:
            return -1
    return 0

def extract_featuresets(ticker):
    tickers, df = process_data_for_labels(ticker)
    
    # TODO refactor this code maybe using a list comprehension
    df['{}_target'.format(ticker)] = list(map(buy_sell_hold, 
                                              df['{}_1d'.format(ticker)],
                                              df['{}_2d'.format(ticker)],
                                              df['{}_3d'.format(ticker)],
                                              df['{}_4d'.format(ticker)],
                                              df['{}_5d'.format(ticker)],
                                              df['{}_6d'.format(ticker)],
                                              df['{}_7d'.format(ticker)],
                                            ))

    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print ('Data spread: ', Counter(str_vals))

    df.fillna(0, inplace=True)
    
    # replace infinite changes with np.nan - e.g. when dealing with 0s in percentages
    df = df.replace([np.inf, -np.inf], np.nan)
    # now drop the NaNs
    df.dropna(inplace=True)

    # which columns get to be the feature sets
    # percent change from yesterday (normalised)
    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    X = df_vals.values
    y = df['{}_target'.format(ticker)].values

    return X, y, df

def do_ml(ticker):
    X, y, df = extract_featuresets(ticker)

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X,
                                                                         y,
                                                                         test_size = 0.25)
    
    # example of a simple classifier
    # clf = neighbors.KNeighborsClassifier()

    # more complicated classifier
    clf = VotingClassifier([('lsvc', svm.LinearSVC()),
                            ('knn', neighbors.KNeighborsClassifier()),
                            ('rfor', RandomForestClassifier())])

    clf.fit(X_train, y_train)

    confidence = clf.score(X_test, y_test)
    predictions = clf.predict(X_test)

    # what kind of predictions are we making
    # are they skewed at all
    # the classifier might just decide on 1 'best' value which is bad
    print ('Accuracy: ', confidence)
    print ('Predicted spread: ', Counter(predictions)) 

    return confidence

do_ml('BAC') 

    