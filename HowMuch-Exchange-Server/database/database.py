# -*- coding: utf-8 -*-

import pymysql
from pymysql import IntegrityError

# Created by planb 2017. 03. 28
# db = Database()
# db.execute("SELECT FROM table_name WHERE column='", column_name, "')")


class Database:
    host = 'localhost'
    user = 'root'
    password = 'dhk0654'
    db = 'howmuch_exchange'
    charset = 'utf8'

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        self.connection = pymysql.connect(host=self.host,
                                          user=self.user,
                                          password=self.password,
                                          db=self.db,
                                          charset=self.charset)

    def execute(self, *args):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        query = ''
        for arg in args:
            query += arg

        try:
            if 'SELECT' in query:
                # SELECT문은 fetchall() 메소드 적용
                cursor.execute(query)
                result = cursor.fetchall()
            else:
                # INSERT, UPDATE, DELETE문은 commit() 메소드 적용
                cursor.execute(query)
                result = self.connection.commit()

            cursor.close()
            return result
        except IntegrityError:
            # 문제 발생 시
            return False
