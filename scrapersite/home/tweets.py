from tweepy import Stream
import tweepy
import pickle
import json
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from more_itertools import unique_everseen
import timeit

ckey = 'JizdgEv8IgqySDL2AEFmaUnYf'
csecret = 'AlVbB3FWMQY4DLyw2h4xYs990ARtBBU1h7yS8DpBdVzjWc0iSI'
atoken = '3398616021-tgYDI0I24l0eHkhYOboA8reg3iJm79GF6BfvOQD'
asecret = 'SzhfEeZt9bQiAhINlNvVir86LYdtyrnVfpVHle2y1EOzc'
t_time = 0

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken, asecret)
#twitterStream = Stream(auth,listener())
api = tweepy.API(auth,wait_on_rate_limit_notify=True)
def find_tweets(tags):
    twitter_data = []
    print(tags)
    keywords = tags
    try:
        for tweet in tweepy.Cursor(api.search,q=keywords).items(100):
            twitter_data.append(tweet.text)
        return twitter_data
    except Exception as e:
        print(str(e))
    

#try:
#    keywords = tags
#    twitterStream.filter(track= keywords)
#except Exception as e:
    #print(str(e))

