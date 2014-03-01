import urllib2,sys
from bs4 import BeautifulSoup, NavigableString
html = urllib2.urlopen('http://www.amazon.com/Motorola-Moto-Global-Unlocked-16GB/product-reviews/B00GWR373M/?showViewpoints=1').read()
#print html
soup = BeautifulSoup(html)
table = soup.find('table',{"id":"productReviews"})
divs=table.find_all('div',{"class":"reviewText"})
for div in divs:
	print div
	print "***********\n"

