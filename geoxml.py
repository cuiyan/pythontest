import urllib
import xml.etree.ElementTree as ET
#url:http://python-data.dr-chuck.net/comments_313639.xml
url = raw_input('Enter url:')
content = urllib.urlopen(url)
data = content.read()

tree = ET.fromstring(data)
sumnum = 0
counts = tree.findall('.//count')
for count in counts:
	sumnum = sumnum+int(count.text)
	
print sumnum