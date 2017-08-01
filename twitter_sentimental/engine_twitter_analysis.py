import tweepy
from textblob import TextBlob

consumer_key = 'NxX1npQXBVGayBBHlOweHfbct'
consumer_secret = 'qccqP3w3309PQIr68MkrehHamAXekBRIAYvd2DoVLnMM12N9pe'

access_token = '204919888-vqDoGlL7TSCSosGWmgrO4ePxxIHJvzTuDNbhoyhO'
access_token_secret = '5QFdnPXkHFxbKsjjsJVM7izcoW2RFqghudiUtAbYJ2SUP'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('trump')

for tweet in public_tweets:
    print tweet.text
    analysis = TextBlob(tweet.text)
    print analysis.sentiment
