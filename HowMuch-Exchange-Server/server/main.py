from account import Account
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Account, '/account')

if __name__ == '__main__':
    print('서버 시작')
    app.run('10.156.145.120')