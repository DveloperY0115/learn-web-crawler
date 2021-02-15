from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError
from bs4 import BeautifulSoup

# exception handling
try:
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
else:
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs)