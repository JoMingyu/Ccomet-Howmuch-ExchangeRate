# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api

from restful_modules import account
from restful_modules import exchange_rate
from restful_modules import option
from restful_modules import statistics
from restful_modules import test

from firebase import parse_and_push_thread
from database import database

app = Flask(__name__)
api = Api(app)

api.add_resource(account.SignUp, '/signup')
api.add_resource(account.SignIn, '/signin')
api.add_resource(option.Option, '/option')
api.add_resource(exchange_rate.ExchangeRate, '/exchange_rate')
api.add_resource(statistics.Statistics, '/statistics')

api.add_resource(test.Test, '/test')


def clear_tables():
    database.Database().execute("delete from account")
    database.Database().execute("delete from options")
    database.Database().execute("delete from registration_ids")

# clear_tables()

if __name__ == '__main__':
    print('-- Server Started')
    parse_and_push_thread.ParseThread().start()
    # 스레드 시작

    app.run(host='10.156.145.120', port=80)
    # app run
