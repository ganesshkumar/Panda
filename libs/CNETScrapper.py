from bs4 import BeautifulSoup

import urllib2

class CNETScrapper:

    def __init__(self,CNET_URL):
        self.product_page=urllib2.urlopen(CNET_URL)
        #product_page=urllib2.urlopen("http://reviews.cnet.com/htc-one/")
        self.product_data=BeautifulSoup(self.product_page.read())

    def get_CNET_rating(self):
        Rating=self.product_data.find("div",{'id':'subRatingModal'}).get_text()
        return Rating.strip().split(' ')[3]

#Rating=product_data.find("div",{'class':'pp-big-star'}).get_text()

