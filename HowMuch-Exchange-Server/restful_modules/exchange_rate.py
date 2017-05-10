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
        self.db.close()

        return data


class ExchangeRateAll(Resource):
    db = database.Database()

    def get(self):
        # 전체 환율 조회
        response_list = list()

        rows = self.db.execute(query_formats.exchange_rate_all_select_format)
        for row in rows:
            data = {'src_nation'    : row['src_nation'],
                    'dst_nation'    : row['dst_nation'],
                    'exchange_rate' : row['exchange_rate']}

            response_list.append(data)

        self.db.close()

        return response_list
