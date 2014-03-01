__author__ = 'anandh&sanjeev'

from bs4 import BeautifulSoup

import urllib2

class FlipKartScrapper:

    def __init__(self,product_pageURL,review_pageURL):
        self.product_page=urllib2.urlopen(product_pageURL)
        self.product_data=BeautifulSoup(self.product_page.read())
        self.review_pageURL=review_pageURL


    def get_review_count(self):
        review_count=self.product_data.find("span",{'itemprop':'review_count'}).get_text()
        print review_count
        return review_count

    def get_Rating(self):
        RatingUserCount=self.product_data.find("span",{'itemprop':'ratingCount'}).get_text()
        print RatingUserCount
        Rating=self.product_data.find("div",{'class':'pp-big-star'}).get_text()
        print Rating


    def get_review_data(self):
        review_count=self.get_review_count();

        file_review=open("Flipkart_Review.txt","a")
        file_review_head=open("Flipkart_Review_Head.txt","a")

        pageNum=0
        while int(pageNum) < int(review_count)/10:
            review_page=urllib2.urlopen(self.review_pageURL+"&start="+str(pageNum))
            review_data= BeautifulSoup(review_page.read())

            for review in review_data.findAll("p",{'class':'line bmargin10'}):
                print review.get_text()
                file_review.write(review.get_text())
                print "--------------------------------------------------------------------"

            for reviewHead in review_data.findAll("div",{'class':'line fk-font-normal bmargin5 dark-gray'}):
                print reviewHead.get_text()
                file_review_head.write(reviewHead.get_text())
                print "--------------------------------------------------------------------"
            pageNum=pageNum+10
        file_review.close()
        file_review_head.close()


'''
alch=AlchemyAPI()

resp=alch.category("text","Nexus 5")

print resp


#print "Sentiment: ", resp["docSentiment"]["type"]
'''