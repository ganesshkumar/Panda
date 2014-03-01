import md5
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
        return [x.find('b').get_text() for x in reviews ]

    def get_detail_reviews(self, soup, md5):
        '''get detailed reviews'''
        details = []
        table = soup.find('table',{"id":"productReviews"})
        divs = table.find_all('div',{"class":"reviewText"})
        for x in divs:
            if md5.new(x.get_text()).hexdigest() == md5:
                break
            details.append(x.get_text())
        return details

    def get_all_reviews(self, md5):
        titles = []
        details = []
        for i in xrange(1, self.number_of_pages+1):
            soup = BeautifulSoup(urllib2.urlopen(self.url+str(i)).read())
            details.extend(self.get_detail_reviews(soup, md5))
            titles.extend(self.get_review_titles(soup))
            if len(details)%10 is not 0:
                titles = titles[:len(details)]
                break

        return {'titles': titles, 'details', details ,'rating': self.get_ratings(), 'md5': md5.new(details[0]).hexdigest()}


