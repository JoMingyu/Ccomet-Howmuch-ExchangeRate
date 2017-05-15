# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource
from support import stastic_data

from database import database


class Statistics(Resource):
    db = database.Database()

    def get(self):
        # 통계적 정보 조회
        src_nation = request.args.get('src_nation')
        dst_nation = request.args.get('dst_nation')
        section = request.args.get('section')

        temp = stastic_data.ExploitRate(src_nation, dst_nation)
        data = temp.get_by_section(int(section))
        response = []

        for d in data:
            temp = dict()
            temp['date'] = d['date'].strftime('%Y-%m-%d')
            temp['exchange_rate'] = d['exchange_rate']
            response.append(temp)

        return response, 200
