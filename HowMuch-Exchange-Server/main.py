# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api

from restful_modules import account
from restful_modules import exchange_rate
from restful_modules import option
from restful_modules import statistics

from firebase import push_thread
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
    push_thread.PushThread().start()
    app.run('10.156.145.120')
