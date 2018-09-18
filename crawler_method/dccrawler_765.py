import requests
from bs4 import BeautifulSoup

def crawl_dcinside_765():
    r = requests.get('http://gall.dcinside.com/mgallery/board/lists/?id=765pro&page=1&exception_mode=recommend', headers={'User-Agent': ''})
    html = r.content
    parsed = BeautifulSoup(html, 'html.parser')
    tbody = parsed.tbody
    try:
        articles = tbody.find_all(class_='ub-content')
    except Exception as e:
        print(e)
        return []
    reformed = []
    for article in articles:
        if article.find(class_='gall_subject').string == '공지':
            continue
        link = 'http://gall.dcinside.com/765pro/' + article['data-no']
        title = article.find(class_='gall_tit').a.text
        date = article.find(class_='gall_date').string
        reformed.append(('765념', title, link, date))
    return reformed

if __name__ == '__main__':
    print(crawl_dcinside_765())
