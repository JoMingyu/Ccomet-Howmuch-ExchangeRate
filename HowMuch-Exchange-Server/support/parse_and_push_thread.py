# -*- coding: utf-8 -*-

import threading
import time, datetime
from support import exchange_rate_parser


class ParseThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.p = exchange_rate_parser.Parser()
        # 파서

        self.parse_count = 1
        # 파싱 카운터

    def run(self):
        time.sleep(1)
        while True:
            print(self.get_current_timestamp(), 'Parse Count', self.parse_count, 'Started')

            for country_code in self.p.code_list:
                json_data = self.p.get_exchange_rate(country_code)
                # 한 code에 대한 환율 정보 json 형태로 get

                rate_list = self.p.process_data(json_data)
                # rate_list = tuples in list, (src, dst, rate)

                self.p.commit_data(rate_list, self.parse_count)
                # 환율 정보 적용

                print(self.get_current_timestamp(), country_code, 'parse success.')

            self.parse_count += 1
            time.sleep(30)

    @staticmethod
    def get_current_timestamp():
        return '[' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ']'


p = ParseThread()
p.start()