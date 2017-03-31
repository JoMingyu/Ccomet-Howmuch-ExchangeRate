import threading
import datetime
import time
from exchange_rate_parser import Parser


class PushThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.last_send = self.current_time()
        self.term = 1
        self.p = Parser()

    def run(self):
        print('Push thread start')
        if self.check_time():
            self.last_send = self.current_time()

            for country in self.p.code_list:

                json_data = self.p.get_exchange_rate(country)
                rate_list = self.p.process_data(json_data)

                for exchange_rate in rate_list:
                    print(exchange_rate)
                    self.p.insert_data(exchange_rate)

        else:
            time.sleep(self.term)

    @staticmethod
    def current_time():
        return datetime.datetime.now()

    def check_time(self):
        current_time = self.current_time()
        time = self.last_send - current_time

        if time.seconds >= 300:
            return True
        else:
            return False
