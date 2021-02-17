from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

nameList = bs.findAll('span', {'class': 'green'})
nameSet = set()

for name in nameList:
    if name.getText() not in nameSet:
        nameSet.add(name.getText())
        print(name.getText())
    else:
        continue