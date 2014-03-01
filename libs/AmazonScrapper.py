import urllib2,sys
from bs4 import BeautifulSoup, NavigableString

class AmazonScrapper:
    def __init__(self, url_first_page):
        self.html = urllib2.urlopen(url_first_page).read()
        self.soup = BeautifulSoup(self.html)
        self.number_of_pages = self.get_number_of_pages()

    def get_number_of_pages(self):
        '''get paging information'''
        pages = self.soup.find('div',{"class":"CMpaginate"})
        links = pages.find_all('a')
        return links[1].get_text()

    def get_review_titles(self):
        '''get single line reviews'''
        reviews = self.soup.find_all('span',{"style":"vertical-align:middle;"})
        #print len(reviews)
        #for review in reviews:
	#    print review.find('b').get_text()
        return [x.find('b').get_text() for x in reviews]

    def get_detail_review(self):
        '''get detailed reviews'''
        table = self.soup.find('table',{"id":"productReviews"})
        divs = table.find_all('div',{"class":"reviewText"})
        return divs
        #print len(divs)
        #for div in divs:
	#    print div
	#    print "***********\n"'''

