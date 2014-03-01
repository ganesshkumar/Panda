import sys
sys.path.append('libs')

from SentimentAnalyser import SentimentAnalyser

senti = SentimentAnalyser()

print senti.get_sentiments(['sanjeev','sanjeev is an asshole','sanjeev is a great guy'])


