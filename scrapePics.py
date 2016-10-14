import urllib
import os
from BeautifulSoup import *

url = raw_input('Enter url:')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
tags = soup.findAll("a", { "share-pic":"1" })
for tag in tags:
	imgurl =  tag.get('href',None)
	imgname = os.path.basename(imgurl)
	#print imgurl
	#print imgname
	urllib.urlretrieve(imgurl,imgname)