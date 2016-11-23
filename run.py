from ircbot import Bot
from crawler import Crawler
from crawler_method.dccrawler import crawl_dcinside
from crawler_method.dccrawler_censored import crawl_dcinside_censored
from crawler_method.dccrawler_765 import crawl_dcinside_765
from crawler_method.dccrawler_765_censored import crawl_dcinside_765_censored
from crawler_method.invencrawler import crawl_inven
from crawler_method.rulicrawler import crawl_ruliweb
from crawler_method.shuneicrawler import crawl_shunei
from crawler_method.yayocrawler import crawl_yayo

from setting import setting_chan_list

bot = Bot.Instance()
crawler_list = [
    Crawler(crawl_dcinside_censored, queue=bot.queue),
    Crawler(crawl_dcinside_765_censored, queue=bot.queue),
    Crawler(crawl_inven, queue=bot.queue),
    Crawler(crawl_ruliweb, queue=bot.queue),
    Crawler(crawl_shunei, queue=bot.queue),
    Crawler(crawl_yayo, queue=bot.queue),
]
specific_crawler_list = [
    Crawler(crawl_dcinside, queue=bot.queue, chan=[setting_chan_list[1][0]]),
    Crawler(crawl_dcinside_765, queue=bot.queue, chan=[setting_chan_list[1][0]]),
]
for crawler in crawler_list + specific_crawler_list:
    crawler.setDaemon(True)
    crawler.start()
bot.start()
