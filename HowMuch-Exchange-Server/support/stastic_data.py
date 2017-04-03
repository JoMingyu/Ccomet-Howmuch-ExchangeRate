import calendar
from time import strftime, localtime

from pandas import DataFrame

from database import Database


class ExploitRate:
    def __init__(self, src, dct):
        self.src = src
        self.dct = dct
        self.db = Database()

    def get_by_section(self, section):
        to_date = strftime("%Y-%m-%d %I:%M", localtime())

        #쿼리를 날릴 때 범위를 정하기 위해 월, 달, 일을 나눔
        day = int(to_date[8:10]) - section
        year = int(to_date[:4])
        month = int(to_date[5:7])

        #현재 일수 보다 범위가 클경우 전달부터 하도록 함 ex) current 10일 범위가 30일경우 전달 20부터 10일까지
        if day < 1:
            if month == 1:
                year -= 1
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

        from_date = to_date[:5] + month + to_date[7:]
        from_date = from_date[:8] + day + from_date[10:]

        #src,dct가 같은 것중 에서 between(from_date ~ to_date)에 대한 정보를 가져옴
        query = "SELECT * FROM test WHERE src='{0}' and dct='{1}' BETWEEN '{2}' and '{3}';"\
                .format(self.src, self.dct, from_date, to_date)
        print(query)#example
        res = self.db.execute(query)

        return res

    #from_date ~ to_date 까지의 환율 정보를 받아 평균을 냄
    def exchange_average(self, data_list):
        count = 0
        sum = 0

        for data in data_list:
            count += 1
            sum += data['rate']

        average = sum / count
        return average

#test
if __name__ == '__main__':
    a = ExploitRate("KRW", "USD")

    temp = a.get_by_section(30)
    data = DataFrame(data=temp, columns=['src', 'dct', 'uploadDate', 'rate'])
    print(data)