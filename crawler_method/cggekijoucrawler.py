import requests
from bs4 import BeautifulSoup

def crawl_cggekijou():
    r = requests.get('http://cggekijo.blog.fc2.com/?xml')
    xml = r.content
    parsed = BeautifulSoup(xml, 'html.parser')
    items = parsed.find_all('item')
    reformed = []
    for item in items:
        link = item.link.string
        title = item.title.contents[0].strip()
        date = item.find('dc:date').string
        reformed.append(('cggekijou', title, link, date))
    return reformed

if __name__ == '__main__':
    print(crawl_cggekijou())
