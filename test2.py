import sys
sys.path.append('libs')

from SentimentAnalyser import SentimentAnalyser

senti = SentimentAnalyser()

print senti.get_text_sentiment('Disappointing service from @Flipkart @flipkartsupport . Have called customer care 3 times in 2 days and still no response from them.')


