import requests
from bs4 import BeautifulSoup

def crawl_dcinside():
    r = requests.get('http://gall.dcinside.com/board/lists/?id=idolmaster&page=1&exception_mode=recommend', headers={'User-Agent': ''})
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
        if article.find(class_='icon_notice') is not None:
            continue
        link = 'http://gall.dcinside.com/idolmaster/' + article['data-no']
        title = article.find(class_='gall_tit').a.text
        date = article.find(class_='gall_date').string
        reformed.append(('@념글', title, link, date))
    return reformed

if __name__ == '__main__':
    print(crawl_dcinside())
