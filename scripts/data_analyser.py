#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:49:21 2018

@author: rjs
"""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

dataset = pd.read_csv('../bases/tweets.csv')
tweets = dataset['Tweets']
classes = dataset['Location']

word_list = [
        'Amoedo é legal', 
        'Amoedo é fraco', 
        'Amoedo será um bom presidente', 
        'Amoedo será o pior presidente',
        '#AmoedoGostoso',
        'Todos com Amoedo',
        'Todos contra Amoedo',
        'Amoedo é inteligente',
        'Amoedo não é inteligente',
        'Amoedo tem boas propostas de governo',
        'Amoedo não tem ideias boas para o governo',
        ]

vectorizer = CountVectorizer(analyzer='word')
# Combine fit and transform into a single step
training_data = vectorizer.fit_transform(word_list)

print(vectorizer.get_feature_names())
print(training_data.toarray())

# Now that we’ve got term counts for each document we can use 
# the TfidfTransformer to calculate the weights for each term in each document

transformer = TfidfTransformer()
calculated_weights = transformer.fit_transform(training_data)
print (calculated_weights)