from flask import Flask
from flask import request, make_response
import database

app = Flask(__name__)

# @app.route('/', methods=['POST', 'GET'])
# def test():
#     return 'success to connect'

db = database.Database()
db.execute('asdf', 'qwe', 'zxcv')

if __name__ == '__main__':
    print('서버 시작')
    app.run('10.156.145.120')