# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource

from database import query_formats
from database import database


class SignUp(Resource):
    # 회원가입
    db = database.Database()

    def post(self):
        connect_sns = request.form['connect_sns']
        client_token = request.form['token']

        if connect_sns == 'True' or connect_sns == 'true':
            # sns 연결 시
            uuid = request.form['uuid']
            google_id = request.form['google_id']

            rows = self.db.execute("SELECT * FROM account WHERE uuid='", uuid, "'")
            if rows:
                # 디바이스에 이미 계정이 생성되어 있을 경우
                return '', 409
            else:
                # 가입되어 있지 않을 때
                self.db.execute(query_formats.register_sns_account_format % (uuid, google_id))
                self.db.execute(query_formats.register_client_token_format % (google_id, client_token))
                return '', 201

        else:
            # sns 미연결 시
            uuid = request.form['uuid']
            id = request.form['id']
            password = request.form['password']

            rows = self.db.execute("SELECT * FROM account WHERE uuid='", uuid, "'")
            if rows:
                # 디바이스에 이미 계정이 생성되어 있을 경우
                return 'conflict uuid', 409
            else:
                # uuid 미중복 시
                rows = self.db.execute("SELECT * FROM account WHERE id='", id, "'")
                if rows:
                    # id 중복 시
                    return 'conflict id', 409
                else:
                    # id 미중복 시
                    if len(password) >= 8:
                        self.db.execute(query_formats.register_account_format % (uuid, id, password))
                        return '', 201
                    else:
                        # 비밀번호 길이가 8자리 미만
                        return '', 409


class SignIn(Resource):
    # 로그인
    # SNS 미연결 시
    db = database.Database()

    def post(self):
        id = request.form['id']
        password = request.form['password']

        rows = self.db.execute("SELECT * FROM account WHERE id='", id, "'")
        if rows:
            # id에 해당하는 계정 존재
            if rows[0]['password'] == password:
                # 로그인 성공
                return '', 201
            else:
                return '', 404
        else:
            # 계정 미존재
            return '', 404
