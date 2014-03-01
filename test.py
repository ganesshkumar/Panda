import sys
sys.path.append('libs')
from AmazonScrapper import AmazonScrapper
from SentimentAnalyser import SentimentAnalyser
from FlipKartScrapper import FlipKartScrapper

amazon = AmazonScrapper('http://www.amazon.com/SUPERSHIELDZ-Definition-Protector-Motorola-Replacements/product-reviews/B00GI3Q4OO/ref=cm_cr_dp_see_all_btm?ie=UTF8&sortBy=bySubmissionDateDescending&showViewpoints=')

flipkart = FlipKartScrapper("http://www.flipkart.com/google-nexus-5/p/itmdq9vxq6nswafg?pid=MOBDQ9VXZMHXZGBP","http://www.flipkart.com/google-nexus-5/product-reviews/ITMDQ9VXQ6NSWAFG?pid=MOBDQ9VXZMHXZGBP&sort_order=most-recent")

senti = SentimentAnalyser()

amazon_reviews = amazon.get_all_reviews('arvind')
flipkart_reviews = flipkart.get_review_data('arvind')

amazon_analysis = senti.get_sentiments(amazon_reviews['titles'])
flipkart_analysis = senti.get_sentiments(flipkart_reviews['titles'])

print amazon_analysis
print flipkart_analysis


