import requests
from bs4 import BeautifulSoup
import pprint
import sys

if sys.argv[1]:
    pages = int(sys.argv[1])
else:
    pages = 1


def fetch_data(page):
    if sys.argv[1]:
        res = requests.get('https://news.ycombinator.com/?p=' + str(page))
    else:
        res = requests.get('https://news.ycombinator.com/news')
    soup = BeautifulSoup(res.text, 'html.parser')

    links = soup.select('.titleline > a')
    subtext = soup.select('.subtext')
    return {'links': links, 'subtext': subtext}


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def creat_custom_dn():
    hn = []
    for page in range(pages):
        data = fetch_data(page + 1)
        links = data['links']
        subtext = data['subtext']
        for idx, item in enumerate(links):
            title = item.getText()
            href = item.get('href', None)
            vote = subtext[idx].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(creat_custom_dn())
