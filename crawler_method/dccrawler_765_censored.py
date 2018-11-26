import requests
from bs4 import BeautifulSoup

def crawl_dcinside_765_censored():
    keywords = ['핫산', '그림', '만화', 'manwha', 'manhwa']
    bad_keywords = ['젖', '좆', '가슴', '노출', '정액', '무현', '찌찌', '자위']
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
        if article.find(class_='gall_num').string == '설문':
            continue
        if article.find(class_='gall_subject').string == '공지':
            continue
        if article.get('data-no', None) is None:
            continue
        link = 'http://gall.dcinside.com/765pro/' + article['data-no']
        title = article.find(class_='gall_tit').a.text
        P = False
        for keyword in keywords:
            P = P or keyword in title
        for badword in bad_keywords:
            P = P and not badword in title
        if not P:
            continue
        date = article.find(class_='gall_date').string
        reformed.append(('765념', title, link, date))
    return reformed

if __name__ == '__main__':
    print(crawl_dcinside_765_censored())
