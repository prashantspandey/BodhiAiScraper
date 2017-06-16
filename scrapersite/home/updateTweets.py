from home.models import Post,Tags,Tweets
from home.tweets import *
from home.tweetsim import *
import numpy as np
import re
from more_itertools import unique_everseen
def update_tweets():
    reg1 = re.compile(r'http(.*?)" "',re.DOTALL)
    reg2 = re.compile('&amp',re.DOTALL)
    po = Post.objects.all().order_by('-pub_date')
    for singlePost in po:
        existing_tweets = []
        if singlePost.tweets_set.all():
            for ch in singlePost.tweets_set.all():
                existing_tweets.append(ch.tweet)
        else:
            tweeting(po,reg1,reg2)
          
def tweeting(po,reg1,reg2):
    for singlePost in po:
        ta = singlePost.tags_set.all()
        tag_list = []
        for j in ta:
            tag_list.append(j.tag)
        tweets = find_tweets(tag_list)
        try:
            if len(tweets)>1:
                tw_index = []
                tw_sim = []
                for tw in range(len(tweets)):
                    for se in range(len(tweets)):
                        if se <= tw:
                            pass
                        else:
                            si = sim(str(tweets[tw]),str(tweets[se]))
                            tw_index.append([tw,se])
                            tw_sim.append(si)
                tweet_similarities = list(zip(tw_index,tw_sim))
                tweet_similarities = np.array(tweet_similarities)
                print(tweet_similarities.shape)
                same_index_tweets = []
                same_tweets = tweet_similarities[:,1]>=0.5
                for n,z in enumerate(same_tweets):
                    if z ==True:
                            same_index_tweets.append(tweet_similarities[n,0])
                same_index_tweets = np.array(same_index_tweets)
                print(same_index_tweets.shape)
                take_repeating = []
                for z in same_index_tweets[:,1]:
                    take_repeating.append(z)
                take_repeating = list(unique_everseen(take_repeating))
                print(take_repeating)
                unique_tweets = []
                for n,z in enumerate(tweets):
                    if n in take_repeating:
                        pass
                    else:
                        unique_tweets.append(z)
                print(len(tweets))
                print(len(take_repeating))
                print(len(unique_tweets))
                #print(unique_tweets)
                #print(take_repeating)
                for k in unique_tweets:
                    similarity = sim(str(singlePost.body),str(k))
                    if similarity>0.2:
                        print('Similarity between %s ------ and %s is :%.2f' %(singlePost.headline,str(k),similarity))
                        k = reg1.sub('',k)
                        k = reg2.sub('',k)
                        newTweet = Tweets(posttweet = singlePost,tweet= k)
                        newTweet.emotion = str(0)
                        newTweet.relavent = similarity
                        newTweet.save()
                    else:
                        print('Not similar enough')
        except Exception as e:
            print(str(e))
