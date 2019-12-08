import spacy
from spacy.lemmatizer import Lemmatizer

lemmatizer = Lemmatizer()
word_list = ['feet', 'foot', 'foots', 'footing']
lemmatized = [lemmatizer.lookup(word) for word in word_list]
print(lemmatized)


print("Test")