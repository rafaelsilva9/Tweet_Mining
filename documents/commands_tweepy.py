#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 12:24:29 2018

@author: rjs
"""

# =============================================================================
# Comandos úteis usando tweepy
# =============================================================================

# =============================================================================
# Locations
# =============================================================================
# u'location': u'Rio de Janeiro, Brazil',
# u'location': u'Brasil, RJ',
# u'location': u'BH',
# u'location': u'Pernambuco',
# u'location': u'Recife, Brazil',
# u'location': u'Recife, Brazil',

# =============================================================================
# Check quantity of queries
# =============================================================================
#api.rate_limit_status()['resources']['search']

# =============================================================================
# Searching with interval date
# =============================================================================
#search_query = '#LulaLivre -filter:retweets'
#tweets_result = tweepy.Cursor(api.search, q=search_query, since='2018-09-15 00:00:00', 
#                              until='2018-09-16 00:00:00').items(1)

# =============================================================================
# Print json
# =============================================================================
#print tweet._json

# =============================================================================
# Get user
# =============================================================================
#user = api.get_user('rafaeljsilva9')
#public_tweets = api.home_timeline()
#print user.screen_name