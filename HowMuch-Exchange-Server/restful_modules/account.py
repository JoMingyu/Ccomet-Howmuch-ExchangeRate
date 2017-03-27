from flask_restful import Resource
from flask import request, make_response
from database import Database

class Account(Resource):
    db = Database()

    def post(self):
        connect_sns = request.form['connect_sns']
        if connect_sns:
            uuid = request.form['uuid']
            rows = self.db.execute("SELECT * FROM account WHERE uuid='", uuid, "'")
            # for row in rows:
            #     print(row)
            result = self.db.execute("INSERT INTO account(uuid, connected_sns) VALUES('", uuid, "', true)")

        else:
            print('asd')