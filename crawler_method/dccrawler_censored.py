import requests
from bs4 import BeautifulSoup

def crawl_dcinside_censored():
    keywords = ['핫산', '그림', '만화']
    r = requests.get('http://gall.dcinside.com/board/lists/?id=idolmaster&page=1&exception_mode=recommend')
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
        link = 'http://gall.dcinside.com/board/view/?id=idolmaster&' + article.find(class_='t_subject').a['href'].split('&')[1]
        title = article.find(class_='t_subject').a.string
        P = False
        for keyword in keywords:
            P = P or keyword in title
        if not P:
            continue
        date = article.find(class_='t_date')['title']
        reformed.append(('@념글', title, link, date))
    return reformed
