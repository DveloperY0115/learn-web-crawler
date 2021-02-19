from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

# set for holding already discovered links at run-time
pages = set()

def get_article_links(wiki_article_url):

    global pages # all function calls share the same set

    # open the given URL and sent HTML request
    html = urlopen('https://en.wikipedia.org{}'.format(wiki_article_url))

    # parse it through BeatifulSoup
    bs = BeautifulSoup(html, 'html.parser')

    return bs.find('div', {'id': 'bodyContent'}).findAll(
        'a', href = re.compile('^(/wiki/)((?!:).)*$'))


def get_links(wiki_article_url):

    global pages

    # open the given URL and sent HTML request
    html = urlopen('https://en.wikipedia.org{}'.format(wiki_article_url))

    # parse it through BeatifulSoup
    bs = BeautifulSoup(html, 'html.parser')

    for link in bs.findAll('a', href=re.compile('^(/wiki/)')):
        # why handle this exception?
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # discovered new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                get_links(newPage)