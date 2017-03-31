import pymysql

class Stat:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',   user='',
                                    password='', db='parser',
                                    charset='utf-8')
        self.curs = self.conn.cursor()

    def set_option(self, src, dct):
        self.src_nation = src
        self.dct_nation = dct


    def get_by_section(self, section):


