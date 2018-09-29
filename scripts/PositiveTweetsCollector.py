#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 00:33:27 2018

@author: rjs
"""
from TweetsCollector import TweetsCollector

class PositiveTweetsCollector:
    
    def create_query_for_positive_tweets(self):
        key_words = ['João Amoêdo', '#VemComJoão30', '#NOVO30', '#ondalaranja', 'JoaoAmoedoNosDebates']
        search_query = ''
    
        for word in key_words:
            if (search_query == ''):
                search_query = word
            else:
                search_query = "%s OR %s -filter:retweets" %(search_query, word)
        return search_query

    def collect_positive_tweets(self):
        collector = TweetsCollector()
        search_query = self.create_query_for_positive_tweets()
        collector.collect(search_query)
