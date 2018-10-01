#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 08:46:02 2018

@author: rjs
"""

from TweetsCollector import TweetsCollector

class NegativeTweetsCollector:
    
    def create_query_for_negative_tweets(self):
        key_words = ['#AmoedoNao',  '#ForaAmoedo', '#ForaNovo', '#NovoNao', '#NovoNunca', 'AmoedoNunca']
        search_query = ''
    
        for word in key_words:
            if (search_query == ''):
                search_query = word
            else:
                search_query = "%s OR %s -filter:retweets" %(search_query, word)
        return search_query

    def collect_negative_tweets(self):
        collector = TweetsCollector()
        search_query = self.create_query_for_negative_tweets()
        
        return collector.collect(search_query)
