import sys
sys.path.append('libs')
from AmazonScrapper import AmazonScrapper
amazon = AmazonScrapper('http://www.amazon.com/SUPERSHIELDZ-Definition-Protector-Motorola-Replacements/product-reviews/B00GI3Q4OO/ref=cm_cr_dp_see_all_btm?ie=UTF8&sortBy=bySubmissionDateDescending&showViewpoints=')

print amazon.get_all_reviews('1b69c097ce38134d7a7eeb6dbbf01ed8')
