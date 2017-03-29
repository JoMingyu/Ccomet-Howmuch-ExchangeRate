import account
import option

from flask import Flask
from flask_restful import Api

from database import Database

app = Flask(__name__)
api = Api(app)

api.add_resource(account.SignUp, '/signup')
api.add_resource(account.SignIn, '/signin')
api.add_resource(option.Option, '/option')

def clear_tables():
    Database().execute("delete from account")
    Database().execute("delete from options")
    Database().execute("delete from registration_ids")

# clear_tables()

if __name__ == '__main__':
    print('서버 시작')
    print('--- resources ---')
    app.run('10.156.145.120')