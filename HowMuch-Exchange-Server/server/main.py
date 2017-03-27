from flask import Flask
from flask import request, make_response
from database import Database

app = Flask(__name__)
db = Database()

# @app.route('/', methods=['POST', 'GET'])
# def test():
#     return 'success to connect'



if __name__ == '__main__':
    print('서버 시작')
    app.run('10.156.145.120')