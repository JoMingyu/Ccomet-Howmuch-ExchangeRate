from flask_restful import Resource
from flask import request, make_response
from database import Database


class SignUp(Resource):
    # 회원가입
    db = Database()

    def post(self):
        connect_sns = request.form['connect_sns']
        if connect_sns:
            uuid = request.form['uuid']

            rows = self.db.execute("SELECT * FROM account WHERE uuid='", uuid, "'")
            if rows:
                # uuid 중복 체크
                return '', 409
            else:
                # 가입되어 있지 않을 때
                result = self.db.execute("INSERT INTO account(uuid, connected_sns) VALUES('", uuid, "', true)")

        else:
            print('asd')

class SignIn(Resource):
    # 로그인
    pass