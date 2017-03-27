from flask_restful import Resource
from flask import request

class Account(Resource):
    def post(self):
        self.connect_sns = request.form['connect_sns']