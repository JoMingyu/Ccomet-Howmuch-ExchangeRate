from flask_restful import Resource
from flask import request
from database import Database

class Option(Resource):
    db = Database()

    def post(self):
        # 옵션 등록

        uuid = request.form['uuid']
        src_nation = request.form['src_nation']
        dst_nation = request.form['dst_nation']

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

            percentage_datum_point = float(request.form['percentage_datum_point'])
            # 기준점(고정값/현재까지 평균/이번주 평균/현재까지 최고가/현재까지 최저가)

            print(fall_percentage, rise_percentage, percentage_datum_point)

            if self.row_exists(uuid, src_nation, dst_nation):
                # 이미 uuid : src_nation-dst_nation에 대응되는 row가 있는 경우
                query = "UPDATE options SET fall_percentage=%f, rise_percentage=%f, percentage_datum_point=%f WHERE uuid='%s' AND src_nation='%s' AND dst_nation='%s'"
                self.db.execute(query % (fall_percentage, rise_percentage, percentage_datum_point, uuid, src_nation, dst_nation))
                return '', 201
            else:
                # row가 없는 경우
                query = "INSERT INTO options(uuid, src_nation, dst_nation, fall_percentage, rise_percentage, percentage_datum_point) VALUES('%s', '%s', '%s', %f, %f, %f)"
                self.db.execute(query % (uuid, src_nation, dst_nation, fall_percentage, rise_percentage, percentage_datum_point))
                return '', 201

        elif option_name == '':
            pass

    @staticmethod
    def row_exists(uuid, src_nation, dst_nation):
        rows = Database().execute("SELECT * FROM options WHERE uuid='", uuid, "' AND src_nation='", src_nation, "' AND dst_nation='", dst_nation, "'")
        if rows:
            return True
        else:
            return False