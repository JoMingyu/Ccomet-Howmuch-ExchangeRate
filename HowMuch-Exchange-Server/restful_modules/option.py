from flask_restful import Resource
from flask import request, json
from database import Database
import query_formats


class Option(Resource):
    db = Database()

    def get(self):
        # 옵션 조회
        uuid = request.args.get('uuid')
        src_nation = request.args.get('src_nation')
        dst_nation = request.args.get('dst_nation')

        if self.row_exists(uuid, src_nation, dst_nation):
            rows = self.db.execute(query_formats.option_select_format % (uuid, src_nation, dst_nation))

            data = {'fall_percentage': rows[0]['fall_percentage'],
                    'rise_percentage': rows[0]['rise_percentage'],
                    'percentage_criteria': rows[0]['percentage_criteria'],
                    'fixed_value_lower_limit': rows[0]['fixed_value_lower_limit'],
                    'fixed_value_upper_limit': rows[0]['fixed_value_upper_limit'],
                    'every_change': rows[0]['every_change'],
                    'every_rise': rows[0]['every_rise'],
                    'every_fall': rows[0]['every_fall']
                    }

            return json.dumps(data), 200
        else:
            return '', 204

    def post(self):
        # 옵션 등록
        uuid = request.form['uuid']
        src_nation = request.form['src_nation']
        dst_nation = request.form['dst_nation']
        # options 테이블을 조작하기 위한 기본 데이터(PK)

        option_name = request.form['option_name']
        if option_name == 'percentage':
            fall_percentage = float(request.form['fall_percentage'])
            # 하락율(%)
            # 미지정 시 0 요청
            # 기준점보다 [fall_percentage]% 떨어졌을 때 푸쉬

            rise_percentage = float(request.form['rise_percentage'])
            # 상승률(%)
            # 미지정 시 0 요청
            # 기준점보다 [rise_percentage]% 올라갔을 때 푸쉬

            percentage_criteria = float(request.form['percentage_criteria'])
            # 기준점(고정값/현재까지 평균/이번주 평균/현재까지 최고가/현재까지 최저가)

            if self.row_exists(uuid, src_nation, dst_nation):
                # 이미 uuid : src_nation-dst_nation에 대응되는 row가 있는 경우
                self.db.execute(query_formats.percentage_update_format % (fall_percentage, rise_percentage, percentage_criteria, uuid, src_nation, dst_nation))
                return '', 201
            else:
                # row가 없는 경우
                self.db.execute(query_formats.percentage_insert_format % (uuid, src_nation, dst_nation, fall_percentage, rise_percentage, percentage_criteria))
                return '', 201

        elif option_name == 'fixed_value':
            fixed_value_lower_limit = float(request.form['fixed_value_lower_limit'])
            # 하한선 아래로 내려갔을 때 푸쉬알림
            # 미지정 시 0 요청
            # [fixed_value_lower_limit] 아래로 환율이 떨어졌을 때 푸쉬

            fixed_value_upper_limit = float(request.form['fixed_value_upper_limit'])
            # 상한선 위로 올라갔을 때 푸쉬알림
            # 미지정 시 0 요청
            # [fixed_value_upper_limit] 위로 환율이 올랐을 때 푸쉬

            if self.row_exists(uuid, src_nation, dst_nation):
                self.db.execute(query_formats.fixed_value_update_format % (fixed_value_lower_limit, fixed_value_upper_limit, uuid, src_nation, dst_nation))
                return '', 201
            else:
                self.db.execute(query_formats.fixed_value_insert_format % (uuid, src_nation, dst_nation, fixed_value_lower_limit, fixed_value_upper_limit))
                return '', 201

        elif option_name == 'boolean_options':
            every_change = request.form['every_change']
            # 모든 변화에서 푸쉬알림

            every_rise = request.form['every_rise']
            # 모든 환율 상승에서 푸쉬알림

            every_fall = request.form['every_fall']
            # 모든 환율 하락에서 푸쉬알림

            if self.row_exists(uuid, src_nation, dst_nation):
                self.db.execute(query_formats.boolean_options_update_format % (every_change, every_rise, every_fall, uuid, src_nation, dst_nation))
                return '', 201
            else:
                self.db.execute(query_formats.boolean_options_insert_format % (uuid, src_nation, dst_nation, every_change, every_rise, every_fall))
                return '', 201

    @staticmethod
    def row_exists(uuid, src_nation, dst_nation):
        query = "SELECT * FROM options WHERE uuid='%s' AND src_nation='%s' AND dst_nation='%s'"
        rows = Database().execute(query % (uuid, src_nation, dst_nation))
        if rows:
            return True
        else:
            return False
