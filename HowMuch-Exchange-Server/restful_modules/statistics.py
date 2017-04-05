# -*- coding: utf-8 -*-

from flask import request, jsonify
from flask_restful import Resource

from database import database


class Statistics(Resource):
    db = database.Database()

    def get(self):
        # 통계적 정보 조회
        src_nation = request.args.get('src_nation')
        dst_nation = request.args.get('dst_nation')
        src_date = request.args.get('src_date')
        dst_date = request.args.get('dst_date')

        # 메소드 호출
        data = []

        return jsonify(result=data)
