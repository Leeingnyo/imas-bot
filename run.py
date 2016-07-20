from ircbot import Bot
from crawler import Crawler
from dccrawler import crawl_dcinside
from invencrawler import crawl_inven
from rulicrawler import crawl_ruliweb
from shuneicrawler import crawl_shunei
from yayocrawler import crawl_yayo

bot = Bot.Instance()
crawler_list = [
    Crawler(crawl_dcinside, queue=bot.queue),
    Crawler(crawl_inven, queue=bot.queue),
    Crawler(crawl_ruliweb, queue=bot.queue),
    Crawler(crawl_shunei, queue=bot.queue),
    Crawler(crawl_yayo, queue=bot.queue),
]
for crawler in crawler_list:
    crawler.setDaemon(True)
    crawler.start()
bot.start()
