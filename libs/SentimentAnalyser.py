import sys
sys.path.append('libs')

from alchemyapi import AlchemyAPI
alchemy=AlchemyAPI()


class SentimentAnalyser

   def __init__(self)




text = "sanjeev is an asshole"
dict = alchemy.sentiment('text',text)
print dict['docSentiment']
 
