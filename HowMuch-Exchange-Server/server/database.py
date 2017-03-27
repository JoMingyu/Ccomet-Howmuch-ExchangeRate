import pymysql

class Database:

    host = 'localhost'
    port = 3306
    user = 'root'
    password = ''
    db = 'howmuch_exchange'
    charset = 'utf8'

    def __init__(self):
        self.connection = pymysql.connect(host=self.host,
                                          port=self.port,
                                          user=self.user,
                                          password=self.password,
                                          db=self.db,
                                          charset=self.charset)
        self.cursor = self.connection.cursor()

    def execute(self, *args):
        self.query = ''
        for arg in args:
            self.query += arg

        return self.cursor.execute(self.query)