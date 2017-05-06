from flask import Flask
from flask_restful import Api

from restful_modules import account
from restful_modules import exchange_rate
from restful_modules import option
from restful_modules import statistics

from firebase import parse_and_push_thread
from database import database

app = Flask(__name__)
api = Api(app)

api.add_resource(account.SignUp, '/signup')
api.add_resource(account.SignIn, '/signin')
api.add_resource(option.Option, '/option')
api.add_resource(exchange_rate.ExchangeRate, '/exchange_rate')
api.add_resource(statistics.Statistics, '/statistics')


def clear_tables():
    database.Database().execute("delete from account")
    database.Database().execute("delete from options")
    database.Database().execute("delete from registration_ids")

# clear_tables()

if __name__ == '__main__':
    print('-- Server Started')
    parse_and_push_thread.ParseThread().start()
    # 스레드 시작

    # app.run(host='10.156.146.155', port=80)