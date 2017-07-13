import requests
from bs4 import BeautifulSoup

def crawl_dcinside_765():
    r = requests.get('http://gall.dcinside.com/mgallery/board/lists/?id=765pro&page=1&exception_mode=recommend', headers={'User-Agent': ''})
    html = r.content
    parsed = BeautifulSoup(html, 'html.parser')
    tbody = parsed.tbody
    try:
        articles = tbody.find_all(class_='tb')
    except Exception as e:
        print(e)
        return []
    reformed = []
    for article in articles:
        if article.find(class_='t_notice').string == '공지':
            continue
        link = 'http://gall.dcinside.com/mgallery/board/view/?id=765pro&' + article.find(class_='t_subject').a['href'].split('&')[1]
        title = article.find(class_='t_subject').a.string
        date = article.find(class_='t_date')['title']
        reformed.append(('765념', title, link, date))
    return reformed
