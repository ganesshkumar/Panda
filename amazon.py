import urllib2,sys
from bs4 import BeautifulSoup, NavigableString
html = urllib2.urlopen('http://www.amazon.com/Motorola-Moto-Global-Unlocked-16GB/product-reviews/B00GWR373M/?showViewpoints=1').read()


soup = BeautifulSoup(html)

#get paging information
pages=soup.find('div',{"class":"CMpaginate"})
links=pages.find_all('a')
print links[1].get_text()


#get single line reviews
#style="vertical-align:middle;"
reviews=soup.find_all('span',{"style":"vertical-align:middle;"})
print len(reviews)
for review in reviews:
	print review.find('b').get_text()


#get detailed reviews
table = soup.find('table',{"id":"productReviews"})
divs=table.find_all('div',{"class":"reviewText"})
print len(divs)
'''for div in divs:
	print div
	print "***********\n"'''

