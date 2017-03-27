import pymysql
from pymysql import IntegrityError

class Database:
    host = 'localhost'
    port = 3306
    user = 'root'
    password = ''
    db = 'howmuch_exchange'
    charset = 'utf8'

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        self.connection = pymysql.connect(host=self.host,
                                          port=self.port,
                                          user=self.user,
                                          password=self.password,
                                          db=self.db,
                                          charset=self.charset)
        self.cursor = self.connection.cursor()

    def execute(self, *args):
        query = ''
        for arg in args:
            query += arg

        try:
            if 'INSERT' in query:
                self.cursor.execute(query)
                result = self.connection.commit()
            elif 'SELECT' in query:
                self.cursor.execute(query)
                result = self.cursor.fetchall()

            return result
        except IntegrityError:
            # 문제 발생 시
            return False