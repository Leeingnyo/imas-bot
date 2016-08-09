from ircbot import Bot
from crawler import Crawler
from crawler_method.dccrawler import crawl_dcinside
from crawler_method.dccrawler_censored import crawl_dcinside_censored
from crawler_method.invencrawler import crawl_inven
from crawler_method.rulicrawler import crawl_ruliweb
from crawler_method.shuneicrawler import crawl_shunei
from crawler_method.yayocrawler import crawl_yayo

bot = Bot.Instance()
crawler_list = [
    Crawler(crawl_dcinside_censored, queue=bot.queue),
    Crawler(crawl_inven, queue=bot.queue),
    Crawler(crawl_ruliweb, queue=bot.queue),
    Crawler(crawl_shunei, queue=bot.queue),
    Crawler(crawl_yayo, queue=bot.queue),
]
for crawler in crawler_list:
    crawler.setDaemon(True)
    crawler.start()
bot.start()
