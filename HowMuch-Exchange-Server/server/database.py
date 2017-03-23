import pymysql

class Database:
    host = 'localhost'
    port = 3306
    user = 'root'
    passwd = ''
    db = 'howmuch_exchange'
    charset = 'utf8'

    def __init__(self):
        self.connection = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset)
        self.cursor = self.connection.cursor()

    def execute(self, *args):
        self.query = ''
        for arg in args:
            self.query += arg

        # print(query)

        return
