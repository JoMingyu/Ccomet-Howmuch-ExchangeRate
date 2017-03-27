from pyfcm import FCMNotification
from database import Database

class FCMSender:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self, server_key):
        self.push_service = FCMNotification(api_key=server_key)
        self.db = Database()

    def send(self):
        registration_ids = list() # DB에서 가져오는 클라이언트 id들


