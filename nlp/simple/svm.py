from nlp_helper_functions import sentence_preprocessing, word_vectorization

import pandas as pd
from sklearn import model_selection, svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score

data_column = 'text'
processed_column = 'text_final'
target = 'target'

Corpus = sentence_preprocessing(pd.read_csv('../disaster-tweets.csv'), data_column, processed_column)

print("Columns: ", Corpus.columns)
print("Split data")
Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(Corpus[processed_column],Corpus[target],test_size=0.3)

(Train_X_Tfidf, Test_X_Tfidf) = word_vectorization(Corpus, processed_column, Train_X, Test_X)

SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
SVM.fit(Train_X_Tfidf,Train_Y)
predictions_SVM = SVM.predict(Test_X_Tfidf)
print("SVM Accuracy Score -> ",accuracy_score(predictions_SVM, Test_Y)*100)