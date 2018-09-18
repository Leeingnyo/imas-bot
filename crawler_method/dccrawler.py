import requests
from bs4 import BeautifulSoup

def crawl_dcinside():
    r = requests.get('http://gall.dcinside.com/board/lists/?id=idolmaster&page=1&exception_mode=recommend', headers={'User-Agent': ''})
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
        date = article.find(class_='t_date')['title']
        reformed.append(('@념글', title, link, date))
    return reformed

if __name__ == '__main__':
    print(crawl_dcinside())
