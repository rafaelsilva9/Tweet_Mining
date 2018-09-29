#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 00:39:48 2018

@author: rjs
"""
import pandas as pd
import tweepy

consumer_key = 'eICGRZ3xMVGAS2LZtW2HZ8ESP'
consumer_secret = 'uaaibUdbfNujAJbaXJ6fZCDoqTPZVapf6iLMSuOl7zvEATfRky'
access_token = '988578283922100225-kGZrxiEFmMNPVlIupkBz45BzCf5n4Dk'
access_token_secret = 'toqhW7r8FfmWQwyf0ebUsQY9tfa2QfUiqHAJYuarET3Br'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class TweetsCollector:
    
    def collect(self, search_query):
        location_list = list()
        tweets_list = list()
        print('Collecting tweets ...')
        tweets_result = tweepy.Cursor(api.search, q=search_query, tweet_mode='extended', 
                                  count=200, lang="pt").items(200)
    
        for tweet in tweets_result:
            if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
                location_list.append(tweet.user.location)
                tweets_list.append(tweet.full_text)
            
        tweets_Dataframe = pd.DataFrame({'Tweets': tweets_list, 'Location': location_list})
        tweets_Dataframe.to_csv('../bases/tweets.csv', encoding='utf-8', index = False)
        print('A file with the collected tweets was generated')