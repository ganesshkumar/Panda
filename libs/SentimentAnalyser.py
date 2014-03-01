import sys

#from DatumBox import DatumBox
from alchemyapi import AlchemyAPI

alchemy=AlchemyAPI()
#datum_box=DatumBox('f78c469c6bb22ee40677b30738d69538')


class SentimentAnalyser:

   def __init__(self):
       pass

   def get_text_sentiment(self, text):
       dict = alchemy.sentiment('text',text)
       if 'docSentiment' in dict:
          return dict['docSentiment']	
       else:
          return {'type':'invalid'}

   def get_sentiments(self,details):
       positive=0
       negative=0 
       neutral=0
       for text in details:
          dict = self.get_text_sentiment(text)
          if dict['type'] == 'positive':
             positive += 1
          elif dict['type'] == 'negative':	
	     negative += 1
          else:
             neutral += 1	
       return {'positive':positive, 'negative':negative, 'neutral':neutral}

   def get_tweet_sentiment(self,tweet):
       return datum_box.twitter_sentiment_analysis(tweet)
        
   def get_tweet_sentiments(self,tweets):
       positive=0
       negative=0 
       neutral=0
       for tweet in tweets:
          result = self.get_tweet_sentiment(tweet)
          if result == 'positive':
             positive += 1
          elif result == 'negative':
             negatvie += 1
          else:
             neutral += 1
       return {'positive':positive, 'negative':negative, 'neutral':neutral} 












  	
