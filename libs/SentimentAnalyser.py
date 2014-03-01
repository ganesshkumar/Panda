import sys
sys.path.append('libs')

from alchemyapi import AlchemyAPI
alchemy=AlchemyAPI()


class SentimentAnalyser:

   def __init__(self):
       pass
	
   def get_text_sentiment(self,text):
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


