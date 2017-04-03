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
        clients_to_push = self.get_clients_to_push(registration_ids, self.db)
        message_title = 'HowMuch? 실시간 환율정보 알리미'
        message_body = '환율 변동 정보가 있습니다!'

        result = self.push_service.notify_multiple_devices(registration_ids=clients_to_push,
                                                           message_title=message_title,
                                                           message_body=message_body)

        return result

    @staticmethod
    def get_clients_to_push(registration_ids, db):
        clients_to_push = list() # DB에서 옵션 확인 후 푸쉬알림을 줄 클라이언트 id 리스트

        for registration_id in registration_ids:
            db.execute()
            # if ~~:
            #     clients_to_push.append(registration_id)

        return clients_to_push