#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:49:34 2020

@author: katerinaroza
"""
#include
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler 
from tweepy import Stream
import tweepy as tw
import time
import pandas as pd
import numpy as np
#importing stopwords is optional, in this case it decreased accuracy


access_token="yout_acess_token"
access_token_secret="your_secret_access_token"
consumer_key="your_consumer_krey"
consumer_secret="your_consumer_secret"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words=['happy']#'astonished','satisfied','delighted','pleased','amused'
date_since='2019-12-15'
#collect tweets

tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(200)
    

class Listener(StreamListener):
    saveFile=open('twitter_.csv','a')
    
    for tweet in tweets:
        saveThis=str(time.time())+'::'+ str(tweet)
        saveFile.write(saveThis)
        saveFile.write('\n')
       

#data=open("twitter_happy.csv",'a')
#comprehensive cleaning
        
 
#def clean_tweet(self, tweet):
   # return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())     
    
#data['Text'] = data['Text'].map(lambda x: clean_tweet(self,tweet))
    