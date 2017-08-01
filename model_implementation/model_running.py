import zerorpc
from sklearn.externals import joblib
import string
from nltk.stem.snowball import SnowballStemmer

class SentimentalAnalysis(object):
    def __init__(self):
        self.vectorizer = joblib.load('tfidf_vectorizer.pkl')
        self.model = joblib.load('sentiment_model.pkl')
        self.stemmer = SnowballStemmer('english')

    def predict_sentence(self, sentence):
        sentence = self.stem_text(sentence)
        sentence_transformed = self.vectorizer.transform([sentence])
        prediction = self.model.predict(sentence_transformed)
        probabilities = self.model.predict_proba(sentence_transformed)
        print 'Sentence Requested: ' + sentence
        return prediction[0], probabilities[0][0], probabilities[0][1]

    def stem_text(self, text):
        words = []
        for word in text.split():
            words.append(self.stemmer.stem(word))
        return string.join(words)

def main():
    s = zerorpc.Server(SentimentalAnalysis())
    s.bind("tcp://*:4242")
    print "Server Running"
    s.run()


if __name__ == "__main__" : main()
