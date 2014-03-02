import sys
sys.path.append('libs')
from SentimentAnalyser import SentimentAnalyser
from FlipKartScrapper import FlipKartScrapper
from AmazonScrapper import AmazonScrapper

amazon = AmazonScrapper('http://www.amazon.com/SUPERSHIELDZ-Definition-Protector-Motorola-Replacements/product-reviews/B00GI3Q4OO/ref=cm_cr_dp_see_all_btm?ie=UTF8&sortBy=bySubmissionDateDescending&showViewpoints=')

#flipkart = FlipKartScrapper("http://www.flipkart.com/micromax-eg111/p/itmdtcz8cksffwuy?pid=MOBDTCX9Y377HCYE","http://www.flipkart.com/micromax-eg111/product-reviews/ITMDTCZ8CKSFFWUY?pid=MOBDTCX9Y377HCYE&sort_order=most-recent")

senti = SentimentAnalyser()

amazon_reviews = amazon.get_all_reviews('arvind')

#flipkart_reviews = flipkart.get_review_data('arvind')

#date=flipkart_reviews['date']




#amazon_analysis = senti.get_sentiments(amazon_reviews['titles'])
#flipkart_analysis = senti.get_sentiments(flipkart_reviews['titles'])

#senti=flipkart_analysis['senti_list']

#date_senti = {}

print amazon_reviews['dates']

'''
for iter in xrange(0,len(date)):
    if date[iter] not in date_senti:
        date_senti[date[iter]]={'Positive':0,'Negative':0,'Neutral':0}

    date_senti[date[iter]][senti[iter]]= int(date_senti[date[iter]][senti[iter]]) + 1

print date_senti
'''

#twitter_analysis = senti.get_sentiments(tweets)


#print amazon_analysis
#print flipkart_analysis
#print twitter_analysis

