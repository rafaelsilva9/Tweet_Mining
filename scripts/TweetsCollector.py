#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 00:39:48 2018

@author: rjs
"""
import tweepy
import re

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
                                  count=6, lang="pt").items(6)
    
        for tweet in tweets_result:
            if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
                location_list.append(tweet.user.location)
                tweets_list.append(self.clean_tweets(tweet.full_text))
        
        print('Tweets coletados')
        
        return tweets_list
    
    def clean_tweets(self, tweet):
        tweet = self.remove_outside_multilingual_plane(tweet)
        tweet = self.remove_links(tweet)
        return tweet
        
    # =============================================================================
    # Remove links
    # =============================================================================
    def remove_links(self, tweet):
        return re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet)
        
    # =========================================================================
    # Strip all characters outside of the Basic Multilingual Plane
    # =========================================================================
    def remove_outside_multilingual_plane(self, tweet):
        tweet = tweet.encode("utf-8")
        pattern = re.compile(u"[^\U00000000-\U0000d7ff\U0000e000-\U0000ffff]", flags=re.UNICODE)
        return pattern.sub(u'', unicode(tweet, 'utf-8'))