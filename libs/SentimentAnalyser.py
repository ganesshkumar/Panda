import sys
import urllib,urllib2
import json


class SentimentAnalyser:

   def __init__(self):
       self.url ='http://sentiment.vivekn.com/api/text/'

   def get_text_sentiment(self, text):
	values = {'txt' : text}
	data = urllib.urlencode(values)
	req = urllib2.Request(self.url, data)
	response = urllib2.urlopen(req)
	sentiment_response = response.read()
	json_sent = json.loads(sentiment_response)
	sentiment = json_sent['result']['sentiment']
	print sentiment
        return sentiment


   def get_sentiments(self,details):
       positive=0
       negative=0 
       neutral=0
       for text in details:
          dict = self.get_text_sentiment(text)
          if dict == 'Positive':
             positive += 1
          elif dict == 'Negative':	
	     negative += 1
          else:
             neutral += 1	
       return {'positive':positive, 'negative':negative, 'neutral':neutral}











  	
