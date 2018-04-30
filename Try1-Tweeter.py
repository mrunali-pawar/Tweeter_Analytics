# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:17:46 2018

@author: India
"""
import numpy as np
import pandas as pd
import re
import warnings

#Visualisation
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from IPython.display import display

from wordcloud import WordCloud, STOPWORDS

#nltk
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import *
from nltk import tokenize

matplotlib.style.use('ggplot')
pd.options.mode.chained_assignment = None
warnings.filterwarnings("ignore")


tweets = pd.read_csv('tweets.csv', encoding = "ISO-8859-1")
del tweets['X']
del tweets['favorited']
del tweets['truncated']
del tweets['isRetweet']
del tweets['retweeted']

sid = SentimentIntensityAnalyzer()
tweets['sentiment_compound_polarity']=tweets.text.apply(lambda x:sid.polarity_scores(x)['compound'])
tweets['sentiment_neutral']=tweets.text.apply(lambda x:sid.polarity_scores(x)['neu'])
tweets['sentiment_negative']=tweets.text.apply(lambda x:sid.polarity_scores(x)['neg'])
tweets['sentiment_pos']=tweets.text.apply(lambda x:sid.polarity_scores(x)['pos'])
tweets['sentiment_type']=''
tweets.loc[tweets.sentiment_compound_polarity>0,'sentiment_type']='POSITIVE'
tweets.loc[tweets.sentiment_compound_polarity==0,'sentiment_type']='NEUTRAL'
tweets.loc[tweets.sentiment_compound_polarity<0,'sentiment_type']='NEGATIVE'
tweets.head()



""" Percentages of Positive Negative and Neutral tweets"""
total_Tweets=tweets['id'].count()
(tweets['sentiment_type'].value_counts()/total_Tweets)*100
tweets.sentiment_type.value_counts().plot(kind='bar',title="sentiment analysis")



""" MOST POPULAR / RETWEETED TWEETS   """
tweet_df = tweets.sort_values(by='retweetCount', ascending=False)
tweet_df = tweet_df.reset_index(drop=True)
print ('Top 10 most retweeted tweets are:')

for i in range(10):
    print (tweet_df['text'].ix[i],'-', tweet_df['retweetCount'].ix[i])
    print ('\n')


