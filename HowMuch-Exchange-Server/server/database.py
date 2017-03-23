import pymysql

class Database:
    host = 'localhost'
    port = 3306
    user = 'root'
    passwd = ''
    db = 'howmuch_exchange'
    charset = 'utf8'

    def __init__(self):
        connection = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset)
        cursor = connection.cursor()

    def execute(self, *args):
        query = ''
        for arg in args:
            query += arg

        # print(query)

        return
