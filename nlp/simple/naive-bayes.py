from nlp_helper_functions import sentence_preprocessing, word_vectorization

import pandas as pd
from sklearn import model_selection, naive_bayes, svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

data_column = 'text'
vectorized_column = 'text_final'
target = 'target'

Corpus = sentence_preprocessing(pd.read_csv('../disaster-tweets.csv'), data_column, vectorized_column)

print("Columns: ", Corpus.columns)

print("Split data")
Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(Corpus[vectorized_column],Corpus[target],test_size=0.3)



# Naive = naive_bayes.MultinomialNB()
# Naive.fit(Train_X_Tfidf,Train_Y)
# predictions_NB = Naive.predict(Test_X_Tfidf)
# print("Naive Bayes Accuracy Score -> ",accuracy_score(predictions_NB, Test_Y)*100)