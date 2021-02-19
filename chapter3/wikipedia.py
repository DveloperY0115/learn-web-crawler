from simple_scraper import *

links_in_eric_idle = find_links('https://en.wikipedia.org/wiki/Eric_Idle')

for link in links_in_eric_idle:
    print(link)
