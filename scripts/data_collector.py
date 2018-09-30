#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 17:10:57 2018

@author: rjs
"""
from PositiveTweetsCollector import PositiveTweetsCollector
from NegativeTweetsCollector import NegativeTweetsCollector
from FileGenerator import FileGenerator

COLLECTED_TWEETS_PATH = '../bases/tweets.csv'

positive_collector = PositiveTweetsCollector()
positive_list = positive_collector.collect_positive_tweets()

negative_collector = NegativeTweetsCollector()
negative_list = negative_collector.collect_negative_tweets()

file_generator =  FileGenerator()
file_generator.create(COLLECTED_TWEETS_PATH, positive_list, negative_list)