from __future__ import division
import sframe
import math
import string
from sklearn.linear_model import LogisticRegression
from time import time
from sklearn.metrics import accuracy_score, recall_score, precision_score
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib

print 'Initializing...'
initial_time = time()
products = sframe.SFrame('dataset.gl/')
print 'Data Loaded'

def remove_punctuation(text):
    import string
    return text.translate(None, string.punctuation)

def stem_text(text):
    words = []
    for word in text.split():
        words.append(stemmer.stem(word))
    return string.join(words)

products['review'] = products['review'].apply(remove_punctuation)
products['sentiment'] = products['rating'].apply(lambda rating : +1 if rating > 3 else -1)

print 'Spliting Data...'
t0 = time()
train_data, test_data = products.random_split(.8, seed=1)
t1 = time()
print 'Data Splited in : ' + str(t1 - t0) + " s."
stemmer = SnowballStemmer('english')

print 'Stemming data...'
t0 = time()
products['review'] = products['review'].apply(stem_text)
t1 = time()
print 'Data Stemmed in : ' + str(t1 - t0) + " s."

tfidf_vectorizer = TfidfVectorizer()

print 'Vectorizing...'
t0 = time()
train_matrix = tfidf_vectorizer.fit_transform(train_data['review'])
test_matrix = tfidf_vectorizer.transform(test_data['review'])
t1 = time()
print 'Vectorizer completed in : ' + str(t1 - t0) + " s."

print 'Training Model...'
t0 = time()
sentiment_model = LogisticRegression()
sentiment_model.fit(train_matrix, train_data['sentiment'])
t1 = time()
print 'Training completed in : ' + str(t1 - t0) + " s."

print 'Testing Model...'
prediction = sentiment_model.predict(test_matrix)
prediction = map(float, prediction)
true_labels = map(float, test_data['sentiment'])
print "Accuracy: " + str(accuracy_score(prediction, true_labels))
print "Recall: " + str(recall_score(prediction, true_labels))
print "Precision: " + str(precision_score(prediction, true_labels))

print 'Exporting Vectorizer and Model...'
print 'Exporting Vectorizer...'
joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.pkl')
print 'Vectorizer Exported'
print 'Exporting Model'
joblib.dump(sentiment_model, 'sentiment_model.pkl')
print 'Model Exported'

final_time = time()

print 'Finished - Total Time ' + str(final_time - initial_time) + " s."
