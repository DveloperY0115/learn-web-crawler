from simple_scraper import *

# generate random state for random selection
random.seed(datetime.datetime.now())

if __name__ == '__main__':
    # start crawling from the landing page of Wikipedia
    get_links('')