# -*- coding: utf-8 -*-

import threading
import time
from support import exchange_rate_parser


class PushThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.term = 5
        self.p = exchange_rate_parser.Parser()
        self.parse_count = 1

    def run(self):
        time.sleep(1)

        print(self.get_current_timestamp(), 'Parse Count', self.parse_count, 'Started')
        self.parse_count += 1

        for country_code in self.p.code_list:
            json_data = self.p.get_exchange_rate(country_code)
            rate_list = self.p.process_data(json_data)

            print(self.get_current_timestamp(), country_code, 'parse success.')

            for exchange_rate in rate_list:
                self.p.commit_data(exchange_rate)

        time.sleep(self.term * 60)

    @staticmethod
    def get_current_timestamp():
        now = time.localtime()
        return '[%02d-%02d %02d:%02d:%02d]' % (now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

if __name__ == '__main__':
    p = PushThread()
    p.start()
