#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:49:21 2018

@author: rjs
"""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt

vectorizer = CountVectorizer(analyzer='word', ngram_range=(1, 2))
transformer = TfidfTransformer()
dataset = pd.read_csv('../bases/classified_tweets.csv')
tweets = dataset['Tweets']
classes = dataset['Classes']

def learn():
    # =============================================================================
    # Combine fit and transform into a single step    
    # =============================================================================
    training_data = vectorizer.fit_transform(tweets)
    
    # =============================================================================
    # Now that we’ve got term counts for each document we can use 
    # the TfidfTransformer to calculate the weights for each term in each document    
    # =============================================================================
    calculated_weights = transformer.fit_transform(training_data)
    
    model = MultinomialNB()
    model.fit(calculated_weights, classes)
    
    return model

def predict(model):
    
    training_data = vectorizer.transform(tweets)
    calculated_weights = transformer.transform(training_data)
    
    predictions = model.predict(calculated_weights)
    return predictions

def viewChart(predictions):
    result = pd.DataFrame({'Tweets':tweets,'Classes':predictions})
    
    plt.figure(figsize=(8, 6))
    result.groupby('Classes').count().plot.bar(ylim=0)
    plt.show()
    
model = learn()
predictions = predict(model)
viewChart(predictions)
