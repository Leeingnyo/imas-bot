import requests
from bs4 import BeautifulSoup

def crawl_ruliweb():
    keywords = ['@', '아이마스', '신데마스', '밀리마스', '밀리', '신데', '푸치', '765', '346', '876', '315', '961']
        # , '마스'
    r = requests.get('http://bbs.ruliweb.com/hobby/board/300064/list??type=default')
    html = r.content
    parsed = BeautifulSoup(html, 'html.parser')
    tbody = parsed.tbody
    articles = tbody.select('tr.table_body')
    reformed = []
    for article in articles:
        if article.select('.divsn strong') is not None:
            continue
        link = article.find(class_='subject').a['href']
        title = article.find(class_='subject').a.string
        P = False
        for keyword in keywords:
            P = P or keyword in title
        if not P:
            continue
        date = article.find(class_='time').string.strip()
        reformed.append(('팬만게', title, link, date))
    return reformed
