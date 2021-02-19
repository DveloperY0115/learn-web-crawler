from simple_scraper import *

# generate random state for random selection
random.seed(datetime.datetime.now())

if __name__ == '__main__':
    links = get_article_links('/wiki/Kevin_Bacon')
    recur_limit = 10
    while len(links) > 0 and recur_limit >= 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        print(newArticle)
        recur_limit -= 1
        links = get_article_links(newArticle)