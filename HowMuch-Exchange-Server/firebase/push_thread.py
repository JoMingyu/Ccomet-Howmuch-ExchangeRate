# -*- coding: utf-8 -*-

import threading
import time
from support import exchange_rate_parser


class PushThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.term = 5
        self.p = exchange_rate_parser.Parser()

    def run(self):
        print('Push thread start')

        for country_code in self.p.code_list:
            json_data = self.p.get_exchange_rate(country_code)
            rate_list = self.p.process_data(json_data)

            for exchange_rate in rate_list:
                print(exchange_rate)
                self.p.commit_data(exchange_rate)

        time.sleep(self.term * 60)

if __name__ == '__main__':
    p = PushThread()
    p.start()