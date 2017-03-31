import threading
import datetime
import time
from exchange_rate_parser import Parser

class PushThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.lastSend = self.current_time()
        self.term = 15
        self.p = Parser()

    def run(self):
        print('Push thread started')
        if self.check_time():
            self.lastSend = self.current_time()

            for code in self.p.code_list:
                currency_data = self.p.get_currency(code)
                currency_list = self.p.process_data(currency_data.decode("utf-8"))

                for currencyInfo in currency_list:
                    print(currencyInfo)
        else:
            time.sleep(self.term)

    @staticmethod
    def current_time():
        return datetime.datetime.now()

    def check_time(self):
        currentTime = self.current_time()
        time = self.lastSend - currentTime

        if time.seconds >= 3600:
            return True
        else:
            return False