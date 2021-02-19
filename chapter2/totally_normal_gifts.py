from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)

print('Items in the table:')

for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)

images = bs.findAll('img', {'src': re.compile('\.\.\/img\/gifts\/img.*\.jpg')})

for image in images:
    print(image['src'])