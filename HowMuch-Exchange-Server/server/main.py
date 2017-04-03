from flask import Flask
from flask_restful import Api

import account
import exchange_rate
import option
from database import Database
from push_thread import PushThread

app = Flask(__name__)
api = Api(app)

api.add_resource(account.SignUp, '/signup')
api.add_resource(account.SignIn, '/signin')
api.add_resource(option.Option, '/option')
api.add_resource(exchange_rate.ExchangeRate, '/exchange_rate')


def clear_tables():
    Database().execute("delete from account")
    Database().execute("delete from options")
    Database().execute("delete from registration_ids")

# clear_tables()

if __name__ == '__main__':
    print('서버 시작')
    PushThread().start()
    app.run('10.156.145.120')