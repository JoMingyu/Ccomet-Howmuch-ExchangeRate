from flask import Flask
from flask import request, make_response
from flask import json
from database import Database

app = Flask(__name__)
db = Database()

# @app.route('/', methods=['POST'])
# def index():
#     tempvalue = 4
#     data = {
#         'test' : tempvalue,
#         'test2' : 'jsondata'
#     }
#     return json.dumps(data, indent=4)

if __name__ == '__main__':
    print('서버 시작')
    app.run('10.156.145.120')