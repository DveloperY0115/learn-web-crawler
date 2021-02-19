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


def get_links(wiki_article_url, recur_limit=10):

    global pages

    # open the given URL and sent HTML request
    html = urlopen('https://en.wikipedia.org{}'.format(wiki_article_url))

    # parse it through BeatifulSoup
    bs = BeautifulSoup(html, 'html.parser')

    try:
        print(bs.h1.get_text())    # title of the article (or page)
        print(bs.find(id = 'mw-content-text').findAll('p')[0])    # 1st paragraph
        print(bs.find(id = 'ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing some data! But nothing happened.')

    for link in bs.findAll('a', href=re.compile('^(/wiki/)')):
        # why handle this exception?
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # discovered new page
                newPage = link.attrs['href']
                print('------------------------\n' + newPage)
                pages.add(newPage)
                recur_limit -= 1

                if recur_limit > 0:
                    get_links(newPage, recur_limit)
                else:
                    return