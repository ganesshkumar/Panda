
from FlipKartScrapper import FlipKartScrapper



fp=FlipKartScrapper("http://www.flipkart.com/google-nexus-5/p/itmdq9vxq6nswafg?pid=MOBDQ9VXZMHXZGBP","http://www.flipkart.com/google-nexus-5/product-reviews/ITMDQ9VXQ6NSWAFG?pid=MOBDQ9VXZMHXZGBP&sort_order=most-recent")

print fp.get_review_data("7054a35c9a520f5b589e6187e06e4894")

#print fp.get_Rating()