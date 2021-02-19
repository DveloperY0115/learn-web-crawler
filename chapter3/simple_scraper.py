from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

def getLinks(wiki_article_url):

    # create an empty list which will be used to store links
    links = []

    # open the given URL and sent HTML request
    html = urlopen('https://en.wikipedia.org{}'.format(wiki_article_url))

    # parse it through BeatifulSoup
    bs = BeautifulSoup(html, 'html.parser')

   return bs.find('div', {'id': 'bodyContent'}).findAll(
        'a', href = re.compile('^(/wiki/)((?!:).)*$')
    )

