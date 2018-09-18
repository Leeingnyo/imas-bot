import requests
from bs4 import BeautifulSoup

def crawl_inven():
    r = requests.get('http://www.inven.co.kr/board/powerbbs.php?come_idx=4103')
    html = r.content
    parsed = BeautifulSoup(html, 'html.parser')
    board = parsed.select_one('form[name=board_list1]')
    if board is None:
        return []
    tbody = parsed.select_one('form[name=board_list1]').tbody
    if tbody is None:
        return []
    articles = tbody.select('tr.ls')
    reformed = []
    for article in articles:
        link = article.find(class_='bbsSubject').a['href']
        title = '  '.join([text.strip() for text in article.find(class_='bbsSubject').a.contents if isinstance(text, str)])
        date = article.find(class_='date').string.strip()
        reformed.append(('inven', title, link, date))
    return reformed
