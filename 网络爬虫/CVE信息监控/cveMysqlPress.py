import mysql.connector as mc
import pysnooper,time
from config import DB_HOST,DB_USER,DB_PASSWORD,DATABASE,SQL_TABLE_CREATED

UPDATETIME = time.strftime('%Y-%m-%d',time.localtime(time.time()))

class cveMysqlPress(object):
    def __init__(self):
        self.db=mc.connect(host=DB_HOST,user=DB_USER, password=DB_PASSWORD, database=DATABASE)
        self.cr=self.db.cursor()
        self.create_table()

    def create_table(self,sql=SQL_TABLE_CREATED):
        self.cr.execute(sql)
        self.db.commit()

    # @pysnooper.snoop()
    def insert_data(self,data):
        sql =f'''INSERT INTO cves (cveId,description,dateEntryCreated,cveDetailUrl) values ("{data.get('cveId')}","{data.get('description')}","{data.get('dateEntryCreated')}","{data.get('cveDetailUrl')}")'''
        if self.check_duplicate(data.get('cveId')):
            self.cr.execute(sql)
            self.db.commit()

    def query_data(self,updatetime=UPDATETIME):
        sql = f"SELECT cveId,description,dateEntryCreated,cveDetailUrl FROM cves WHERE updatetime LIKE '{updatetime}%'"
        self.cr.execute(sql)
        return self.cr.fetchall()

    def check_duplicate(self,cveId):
        sql = f"SELECT 1 FROM cves WHERE cveId = '{cveId}'"
        self.cr.execute(sql)
        return False if self.cr.fetchall() else True # 存在返回False 

    def close(self):
        self.db.close()
