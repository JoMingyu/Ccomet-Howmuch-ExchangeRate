# -*- coding: utf-8 -*-

import calendar
from time import strftime, localtime

from database.database import Database
from database import query_formats

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
        query = query_formats.daily_exchange_rate_select_format % (self.src, self.dst, from_date)
        res = self.db.execute(query)

        return res


#test
#
# print(receive_data)
