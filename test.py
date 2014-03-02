import sys
sys.path.append('libs')
from AmazonScrapper import AmazonScrapper
from SentimentAnalyser import SentimentAnalyser
from FlipKartScrapper import FlipKartScrapper
from TwitterAPISearch import TwitterAPISearch
from FunctionExtractor import FunctionExtractor

amazon = AmazonScrapper('http://www.amazon.com/SUPERSHIELDZ-Definition-Protector-Motorola-Replacements/product-reviews/B00GI3Q4OO/ref=cm_cr_dp_see_all_btm?ie=UTF8&sortBy=bySubmissionDateDescending&showViewpoints=')

#flipkart = FlipKartScrapper("http://www.flipkart.com/google-nexus-5/p/itmdq9vxq6nswafg?pid=MOBDQ9VXZMHXZGBP","http://www.flipkart.com/google-nexus-5/product-reviews/ITMDQ9VXQ6NSWAFG?pid=MOBDQ9VXZMHXZGBP&sort_order=most-recent")

#twitter = TwitterAPISearch()

#tweets = twitter.twitterSearch('nexus 5',100)

#func = FunctionExtractor()

#senti = SentimentAnalyser()

amazon_reviews = amazon.get_all_reviews('arvind')
print amazon_reviews['dates']

#flipkart_reviews = flipkart.get_review_data('arvind')
#features1 = func.function_analysis_new(flipkart_reviews)
#features2 = func.function_analysis_new(amazon_reviews)
#features3 = func.function_analysis_new(tweets)
#print "***"
#print flipkart_reviews
#print amazon_reviews
#print tweets

#print func.calculate_features(flipkart_reviews,amazon_reviews,tweets)

#amazon_analysis = senti.get_sentiments(amazon_reviews['titles'])
#flipkart_analysis = senti.get_sentiments(flipkart_reviews['titles'])
#twitter_analysis = senti.get_sentiments(tweets)


#print amazon_analysis
#print flipkart_analysis
#print twitter_analysis

