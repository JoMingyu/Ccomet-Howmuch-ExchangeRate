# -*- coding: utf-8 -*-

from pyfcm import FCMNotification

from database import database
from database import query_formats


class FCMSender:
    def __init__(self, server_key):
        self.push_service = FCMNotification(api_key=server_key)
        self.db = database.Database()

    def send(self, src_nation, dst_nation, old_rate, new_rate):
        clients_to_push = self.get_clients_to_push(src_nation, dst_nation, old_rate, new_rate)
        message_title = 'HowMuch? 실시간 환율정보 알리미'
        message_body = '환율 변동 정보가 있습니다!'
        if len(clients_to_push) == 0:
            pass
        else:
            print(clients_to_push)
            result = self.push_service.notify_multiple_devices(registration_ids=clients_to_push,
                                                               message_title=message_title,
                                                               message_body=message_body)
            print(result)

    # def get_clients_to_push(self, src_nation, dst_nation, old_rate, new_rate):
    def get_clients_to_push(self, src_nation, dst_nation, old_rate, new_rate):
        clients_to_push = list()
        clients = self.db.execute("SELECT * FROM client_tokens")

        if src_nation == 'CAD' and dst_nation == 'ARS':
            clients_to_push.append('coLv0q-qezA:APA91bFlZxDKqBdRlREiE2Iv--d5o1KM3xrf8U8XnuAFUfMmke1sJ4rUPuqTr5hBbMqEwGp16TSTsYmkv4M1ZcYBqFzvfpa_Y_tPt8V1UV9mdpt4pLJjCfyHYHqJKfkw7PCb5Mtga7E1')

        for client in clients:
            id = client['id']
            token = client['client_token']
            options = self.db.execute(query_formats.option_select_format % (id, src_nation, dst_nation))
            for option in options:
                fall_percentage = float(option['fall_percentage'])
                rise_percentage = float(option['rise_percentage'])
                percentage_criteria = float(option['percentage_criteria'])

                fixed_value_lower_limit = float(option['fixed_value_lower_limit'])
                fixed_value_upper_limit = float(option['fixed_value_upper_limit'])

                every_change = option['every_change']
                every_rise = option['every_rise']
                every_fall = option['every_fall']

                if (fall_percentage is not -1 and new_rate < percentage_criteria * ((100 - fall_percentage) / 100)) \
                        or (rise_percentage is not -1 and new_rate > percentage_criteria * ((100 + rise_percentage) / 100)) \
                        or (fixed_value_lower_limit is not -1 and new_rate < fixed_value_lower_limit) \
                        or (fixed_value_upper_limit is not -1 and new_rate > fixed_value_upper_limit) \
                        or every_change or (new_rate > old_rate and every_rise) \
                        or (new_rate < old_rate and every_fall) :
                    clients_to_push.append(token)

        return clients_to_push
