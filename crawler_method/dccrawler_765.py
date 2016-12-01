import requests
from bs4 import BeautifulSoup

def crawl_dcinside_765():
    r = requests.get('http://gall.dcinside.com/mgallery/board/lists/?id=765pro&page=1&exception_mode=recommend')
    html = r.content
    parsed = BeautifulSoup(html, 'html.parser')
    tbody = parsed.tbody
    articles = tbody.find_all(class_='tb')
    reformed = []
    for article in articles:
        if article.find(class_='t_notice').string == '공지':
            continue
        link = 'http://gall.dcinside.com/mgallery/board/view/?id=765pro&' + article.find(class_='t_subject').a['href'].split('&')[1]
        title = article.find(class_='t_subject').a.string
        date = article.find(class_='t_date')['title']
        reformed.append(('765념', title, link, date))
    return reformed