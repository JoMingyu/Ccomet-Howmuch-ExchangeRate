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
                currencyData = self.p.get_currency(code)
                currencyList = self.p.process_data(currencyData)

                for currencyInfo in currencyList:
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