from FlipKartScrapper import FlipKartScrapper

fp=FlipKartScrapper("http://www.flipkart.com/samsung-galaxy-note-3-n9000/p/itmdzq2fypbmmygu?pid=MOBDZQ2EGPHQPJCH","http://www.flipkart.com/samsung-galaxy-note-3-n9000/product-reviews/ITMDZQ2FYPBMMYGU?pid=MOBDZQ2EGPHQPJCH&sort_order=most-recent")

print fp.get_review_data("7054a35c9a520f5b589e6187e06e4894")
