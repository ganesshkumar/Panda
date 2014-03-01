import urllib2,sys
from bs4 import BeautifulSoup, NavigableString
html = urllib2.urlopen('http://www.amazon.com/Motorola-Moto-Global-Unlocked-16GB/product-reviews/B00GWR373M/?showViewpoints=1').read()
#print html
soup = BeautifulSoup(html)
tables = soup.find_all('table')
for table in tables:
	divs=table.find_all('div',{"class":"reviewText"})
	for div in divs:
		print div
		print "***********\n"

