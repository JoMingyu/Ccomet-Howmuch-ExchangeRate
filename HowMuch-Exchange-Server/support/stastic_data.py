# -*- coding: utf-8 -*-

import calendar
from PIL import Image
import io
from time import strftime, localtime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from database.database import Database


class ExploitRate:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.db = Database()

    def get_by_section(self, section):
        current_date = strftime("%Y-%m-%d", localtime())

        # 쿼리를 날릴 때 범위를 정하기 위해 월, 달, 일을 나눔
        day = int(current_date[8:10]) - section
        year = int(current_date[:4])
        month = int(current_date[5:7])

        # 현재 일수 보다 범위가 클경우 전달부터 하도록 함 ex) current 10일 범위가 30일경우 전달 20부터 10일까지
        if day < 1:
            if month == 1:
                month = 12
            else:
                month -= 1

            day = calendar.monthrange(year, month)[1] + day

        if month < 10:
            month = "0" + str(month)
        if day < 10:
            day = "0" + str(day)
        else:
            day = str(day)

        from_date = current_date[:5] + month + current_date[7:]
        from_date = from_date[:8] + day + from_date[10:]

        # src,dct가 같은 것중 에서 between(from_date ~ current_date)에 대한 정보를 가져옴
        query = "SELECT * FROM daily_exchange_rate WHERE src_nation='{0}' and dst_nation='{1}' AND date > '{2}';" \
            .format(self.src, self.dst, from_date)
        res = self.db.execute(query)

        return res


#test
# temp = stastic_data.ExploitRate('ARS', 'AUD')
# data = temp.get_by_section(7)
# receive_data = list()
#
# for i in data:
#     temp = dict()
#     temp['date'] = i['date'].strftime('%Y-%m-%d')
#     temp['exchange_rate'] = i['exchange_rate']
#     receive_data.append(temp)
#
# print(receive_data)
