import sys
sys.path.append('libs')
from AmazonScrapper import AmazonScrapper
amazon = AmazonScrapper('http://www.amazon.com/Motorola-Moto-Global-Unlocked-16GB/product-reviews/B00GWR373M/?showViewpoints=')

print amazon.get_ratings()
