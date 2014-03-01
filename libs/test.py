from AmazonScrapper import AmazonScrapper

test = AmazonScrapper('http://www.amazon.com/SUPERSHIELDZ-Definition-Protector-Motorola-Replacements/product-reviews/B00GI3Q4OO/ref=cm_cr_dp_see_all_btm?showViewpoints=')
res = test.get_all_detail_reviews()
print res
