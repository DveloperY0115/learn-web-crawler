from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

# exception handling
try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
else:
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs)