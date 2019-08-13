import pymysql
import pandas as pd
from dotenv import load_dotenv,find_dotenv
import os
load_dotenv(find_dotenv())
class MysqlConn(object):
    def __init__(self):
        self.conn = pymysql.connect(host=os.getenv("host"),
                                user=os.getenv("user"),
                                password=os.getenv("password"),
                                db=os.getenv("db"),
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    def get_dataframe(self,query):
        return pd.read_sql(con=self.conn,sql=query)