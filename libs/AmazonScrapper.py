import urllib2,sys
from bs4 import BeautifulSoup, NavigableString

class AmazonScrapper:
    def __init__(self, url_first_page):
        self.url = url_first_page
        self.html = urllib2.urlopen(url_first_page+'1').read()
        self.soup = BeautifulSoup(self.html)
        self.number_of_pages = int(self.get_number_of_pages())
        self.ti

    def get_ratings(self):
        '''get rating information'''
        rating = self.soup.find('span',{"class":"swSprite s_star_4_5 "})
        return rating.get_text().split(' ')[0]

    def get_number_of_pages(self):
        '''get paging information'''
        pages = self.soup.find('div',{"class":"CMpaginate"})
        links = pages.find_all('a')
        return links[1].get_text()

    def get_review_titles(self, soup):
        '''get single line reviews'''
        reviews = soup.find_all('span',{"style":"vertical-align:middle;"})
        return [x.find('b').get_text() for x in reviews]

    def get_detail_reviews(self, soup):
        '''get detailed reviews'''
        table = soup.find('table',{"id":"productReviews"})
        divs = table.find_all('div',{"class":"reviewText"})
        return [x.get_text() for x in divs]

    def get_all_reviews(self):
        titles = []
        details = []
        for i in xrange(1, self.number_of_pages+1):
            soup = BeautifulSoup(urllib2.urlopen(self.url+str(i)).read())
            titles.extend(self.get_review_titles(soup))
            details.extend(self.get_detail_reviews(soup))
        return {'titles': titles, 'details', details ,'rating': self.get_ratings()}


