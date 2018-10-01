#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 09:01:53 2018

@author: rjs
"""
import pandas as pd

class FileGenerator:
    def create(self, path, positive_list, negative_list):
        tweets_list = list()
        class_list = list()
        
        self.append_tweets(positive_list, 'A FAVOR', tweets_list, class_list)
        self.append_tweets(negative_list, 'CONTRA', tweets_list, class_list)
        
        tweets_Dataframe = pd.DataFrame({'Tweets': tweets_list, 'Classes': class_list})
        tweets_Dataframe.to_csv(path, encoding='utf-8', index = False)
        print('A file with the collected tweets was generated')
    
    def append_tweets(self, tweetsToAppend, tweetClass, tweets_list, class_list):
        for tweet in tweetsToAppend:
            tweets_list.append(tweet)
            class_list.append(tweetClass)