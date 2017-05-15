from flask import Flask
from flask_restful import Api

from database import database
from restful_modules import account
from restful_modules import exchange_rate
from restful_modules import option
from restful_modules import statistics
from support import parse_and_push_thread
from support import stastic_data

app = Flask(__name__)
api = Api(app)

api.add_resource(account.SignUp, '/signup')
api.add_resource(account.SignIn, '/signin')
api.add_resource(option.Option, '/option')
api.add_resource(exchange_rate.ExchangeRate, '/exchange_rate')
api.add_resource(exchange_rate.ExchangeRateAll, '/exchange_rate/all')
api.add_resource(statistics.Statistics, '/statistics')


def clear_tables():
    database.Database().execute("delete from account")
    database.Database().execute("delete from options")
    database.Database().execute("delete from registration_ids")

# clear_tables()

if __name__ == '__main__':
    # print('-- Server Started')
    # parse_and_push_thread.ParseThread().start()
    # 스레드 시작


        # app.run(host='localhost', port=80)


#그래프에 쓸 데이터 예시
# temp = stastic_data.ExploitRate('ARS', 'AUD')
# data = temp.get_by_section(7)
# receive_data = list()
#
# for i in data:
#     temp = dict()
#     temp['date'] = i['date'].strftime('%Y-%m-%d')
#     temp['exchange_rate'] = i['exchange_rate']
#     receive_data.append(temp)

