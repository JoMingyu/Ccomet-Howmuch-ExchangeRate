# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource

from database import query_formats
from database import database


class ExchangeRate(Resource):
    db = database.Database()

    def get(self):
        # 환율 조회
        src_nation = request.args.get('src_nation')
        dst_nation = request.args.get('dst_nation')

        if src_nation == dst_nation:
            rows = self.db.execute(query_formats.identical_code_select_format % (src_nation))
        else:
            rows = self.db.execute(query_formats.exchange_rate_select_format % (src_nation, dst_nation))

        data = {'exchange_rate': rows[0]['exchange_rate']}

        return data
