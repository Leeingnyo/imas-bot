import requests
from bs4 import BeautifulSoup

def crawl_shunei():
    r = requests.get('http://rss.egloos.com/blog/shunei')
    xml = r.content
    parsed = BeautifulSoup(xml, 'html.parser')
    items = parsed.find_all('item')
    reformed = []
    for item in items:
        categories = item.find_all('category')
        categories_contents = [category.string for category in categories]
        important = False
        for contents in categories_contents:
            important = important or contents == '아이돌마스터'
        for contents in categories_contents:
            important = important or not contents == '잡담'
        if not important:
            continue
        link = item.link.string
        title = item.title.contents[0].strip()
        date = item.pubdate.string
        reformed.append(('shunei', title, link, date))
    return reformed
