#-*- coding: utf-8 -*-

import re
import random
import threading
from datetime import datetime, timedelta
from queue import Queue, Empty

from singleton import Singleton
from connector.ircmessage import IRCMessage
from setting import setting_chan_list

@Singleton
class Bot(threading.Thread):
    irc = None
    queue = Queue()
    chan_list = setting_chan_list

    def __init__(self):
        threading.Thread.__init__(self)

    def init(self):
        for c in self.chan_list:
            self.irc.joinchan(' '.join(c).strip())

    def run(self):
        from connector.ircconnector import IRCConnector
        self.irc = IRCConnector(self.queue)
        self.irc.start()
        self.init()
        prev_date = datetime.now()
        while True:
            try:
                packet = self.queue.get(timeout=2)
            except Empty:
                packet = None

            if packet is None:
                continue
            elif packet['type'] == 'irc':
                message = packet['content']
            elif packet['type'] == 'msg':
                print('get')
                chan_list = self.chan_list
                if packet['chan'] is not None:
                    chan_list = packet['chan']
                for c in chan_list:
                    self.irc.sendmsg(c[0], packet['content'])

if __name__ == '__main__':
    bot = Bot.Instance()
    bot.start()
