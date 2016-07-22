import threading
from time import sleep
from queue import Queue

class Crawler(threading.Thread):

    def __init__(self, method, period=60, queue=None, maximum=40):
        """
        method should return
        list((prefix, title, link, date))
        which of element makes
        prefix| title link (date)
        """
        threading.Thread.__init__(self)
        self.method = method
        self.period = period
        self.queue = queue
        self.maximum = maximum
        self.prev_list = method()
        self.prev_list.reverse()

    def crawl(self):
        recent_list = self.method()
        prev_link = [prev[2] for prev in self.prev_list]
        recent_link = [recent[2] for recent in recent_list]
        # push only new article
        new_link = [link for link in recent_link if link not in prev_link]
        new_list = [recent for recent in recent_list if recent[2] in new_link]
        new_list.reverse()

        for new in new_list:
            info = '%s| %s %s (%s)' % new
            if self.queue is not None:
                self.queue.put({'type': 'msg', 'content': info})
            else:
                print(info)
        self.prev_list = self.prev_list + new_list
        self.prev_list = self.prev_list[-self.maximum:]

    def run(self):
        while True:
            try:
                self.crawl()
            except Exception as e:
                print(e)
            sleep(self.period)
