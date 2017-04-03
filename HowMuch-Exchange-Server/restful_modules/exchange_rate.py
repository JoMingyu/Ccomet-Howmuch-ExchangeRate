from flask import request, json
from flask_restful import Resource

from database import query_formats
from database.database import Database


class ExchangeRate(Resource):
    db = Database()

    def get(self):
        # 환율 조회
        src_nation = request.args.get('src_nation')
        dst_nation = request.args.get('dst_nation')

        rows = self.db.execute(query_formats.exchange_rate_select_format % (src_nation, dst_nation))
        data = {'exchange_rate': rows[0]['exchange_rate']}

        return json.dumps(data), 200