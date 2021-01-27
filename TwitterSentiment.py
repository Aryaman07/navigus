import tweepy
from textblob import TextBlob

consumer_key= "PM0WOeSfGjg5FLtSkdeAhqHXt"
consumer_key_secret= "s9ZzGZqBgSpjzQoY0rcuJXOj0tJ6ZqhJMvrNszse13dqFhpmZ5"
access_token= "1183299959925248001-2dzurQvdh9lq4leU7f6et2yCrUBp4j"
access_token_secret= "STSM7VLsvyNLzNn8KykCiytdj7hHpEnusIpmKPgcdeEaL"

auth=tweepy.OAuthHandler(consumer_key,consumer_key_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
public_tweets=api.search("Sushant Singh Rajput")

for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
    
    if(analysis.sentiment[0]>0):
        print('Positive')
    elif(analysis.sentiment[0]<0):
        print('Negative')
    else:
        print('Neutral')