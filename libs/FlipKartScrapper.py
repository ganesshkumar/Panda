__author__ = 'anandh&sanjeev'

from bs4 import BeautifulSoup

import urllib2
import md5
import unicodedata

class FlipKartScrapper:

    def __init__(self,product_pageURL,review_pageURL):
        print product_pageURL
        self.product_page=urllib2.urlopen(product_pageURL)
        self.product_data=BeautifulSoup(self.product_page.read())
        #print self.product_data
        self.review_pageURL=review_pageURL

    def get_review_count(self):
        review_count=self.product_data.find("span",{'itemprop':'reviewCount'}).get_text()
        return review_count

    def get_Rating(self):
        RatingUserCount=self.product_data.find("span",{'itemprop':'ratingCount'}).get_text()
        Rating=self.product_data.find("div",{'class':'pp-big-star'}).get_text()
        return Rating

    def get_review_data(self,latestMD5):
        flag = 0
        review_count=self.get_review_count();
        print review_count
        flipkart_review = []
        flipkart_review_header = []
        pageNum=0
        while int(pageNum) < int(review_count) and flag == 0:
            print pageNum
            review_page=urllib2.urlopen(self.review_pageURL+"&start="+str(pageNum))

            review_data= BeautifulSoup(review_page.read())

            for review in review_data.findAll("p",{'class':'line bmargin10'}):

                newHash = unicodedata.normalize('NFKD', review.get_text().strip()).encode('ascii','ignore')
                #print md5.new(newHash).hexdigest()
                if md5.new(newHash).hexdigest() == latestMD5:
                    flag=1
                    break
                flipkart_review.append(review.get_text().strip())
                #print "--------------------------------------------------------------------"

            for reviewHead in review_data.findAll("div",{'class':'line fk-font-normal bmargin5 dark-gray'}):
                if len(flipkart_review) == len(flipkart_review_header):
                    break
                flipkart_review_header.append(reviewHead.get_text().strip())

                #print "--------------------------------------------------------------------"
            pageNum=pageNum+10

        if len(flipkart_review) != 0:
            newHash = unicodedata.normalize('NFKD', flipkart_review[0]).encode('ascii','ignore')
            sendMD5 = md5.new(newHash).hexdigest()
        else:
            sendMD5=latestMD5

        return {'titles': flipkart_review_header, 'details': flipkart_review ,'rating': self.get_Rating(), 'md5':sendMD5}

'''
alch=AlchemyAPI()

resp=alch.category("text","Nexus 5")

print resp


#print "Sentiment: ", resp["docSentiment"]["type"]
'''
