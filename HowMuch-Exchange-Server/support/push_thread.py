import threading
import datetime
import time

class Push(threading.Thread):
    def __init__(self):
        self.lastSend = self.current_time()
        self.term = 15

    def run(self):
        if self.check_time():
            self.lastSend = self.current_time()
            #실행할 코드들
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

