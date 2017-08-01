from __future__ import division
import sframe
import math
import string
from sklearn.ensemble import RandomForestClassifier
from time import time
from sklearn.metrics import accuracy_score, recall_score, precision_score, roc_auc_score
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

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
products['sentiment'] = products['rating'].apply(lambda rating : 1 if rating > 3 else -1)

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

tfidf_vectorizer = TfidfVectorizer(stop_words = 'english')
print 'Vectorizing...'
t0 = time()
train_matrix = tfidf_vectorizer.fit_transform(train_data['review'])
test_matrix = tfidf_vectorizer.transform(test_data['review'])
t1 = time()
print 'Vectorizer completed in : ' + str(t1 - t0) + " s."


pca = TruncatedSVD(n_components=1000, random_state=42)
print "Fitting SVD..."
t0 = time()
pca.fit(train_matrix)
t1 = time()
print 'SVD completed in : ' + str(t1 - t0) + " s."


print 'Transforming data to SVD...'
t0 = time()
train_matrix = pca.transform(train_matrix)
test_matrix = pca.transform(test_matrix)
t1 = time()
print 'Transformation completed in : ' + str(t1 - t0) + " s."


print 'Training Model...'
t0 = time()
classifier = RandomForestClassifier(n_estimators=500, max_features=0.1)
classifier.fit(train_matrix, train_data['sentiment'])
t1 = time()
print 'Training completed in : ' + str(t1 - t0) + " s."

print 'Testing Model...'
prediction = classifier.predict(test_matrix)
prediction = map(float, prediction)
true_labels = map(float, test_data['sentiment'])
print "Accuracy: " + str(accuracy_score(prediction, true_labels))
print "Recall: " + str(recall_score(prediction, true_labels))
print "Precision: " + str(precision_score(prediction, true_labels))
print "Area Under Curve: " + str(roc_auc_score(prediction, true_labels))
