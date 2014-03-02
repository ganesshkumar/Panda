__author__ = 'anandh&sanjeev'

from bs4 import BeautifulSoup

import urllib2
import md5
import unicodedata
import time

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
        monthDict={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
        review_count=self.get_review_count();
        print review_count
        flipkart_review = []
        flipkart_review_header = []
        flipkart_review_date = []
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

            for reviewDate in review_data.findAll("div",{'class':'date line fk-font-small'}):
                if len(flipkart_review) == len(flipkart_review_date):
                    break
                month=monthDict[reviewDate.get_text().strip().split(' ')[1]]
                revDate=reviewDate.get_text().strip().split(' ')[0]+'-'+str(month)+'-20'+reviewDate.get_text().strip().split(' ')[2]

                format = '%d-%m-%Y'
                revDate_epoch=time.mktime(time.strptime(revDate, format))

                flipkart_review_date.append(revDate_epoch)

                #print "--------------------------------------------------------------------"
            pageNum=pageNum+10

        print len(flipkart_review)
        print len(flipkart_review_header)
        print len(flipkart_review_date)

        if len(flipkart_review) != 0:
            newHash = unicodedata.normalize('NFKD', flipkart_review[0]).encode('ascii','ignore')
            sendMD5 = md5.new(newHash).hexdigest()
        else:
            sendMD5=latestMD5

        return {'titles': flipkart_review_header, 'details': flipkart_review ,'rating': self.get_Rating(), 'md5':sendMD5, 'date': flipkart_review_date}

'''
alch=AlchemyAPI()

resp=alch.category("text","Nexus 5")

print resp


#print "Sentiment: ", resp["docSentiment"]["type"]
'''
