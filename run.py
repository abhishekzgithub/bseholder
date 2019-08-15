from main import *
from db_utlity import *
import requests
from lxml import html
import logging
import utility
from traceback import format_exc
from pdb import set_trace

logging.basicConfig(filename='output.log',filemode='w',level=logging.INFO,format=utility.LOG_FORMAT)

#URL=f'https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd={BSETicker}&qtrid={period_id}

#get the bseticker id from the database
# sql_obj=SQlAlchemyOperation()
# tmp_table_conn=sql_obj.get_sqlalchemy_conn(database_name="tmp")
# pymysql_obj=MysqlConn()
# conn=pymysql_obj.pymysql_connect()
#df_bseid_qtrid=pymysql_obj.pymysql_get_dataframe(query=utility.q,conn=conn)
#df_bseid_qtrid.to_csv("df_bseid_qtrid.csv",index=False)
df_bseid_qtrid=pd.read_csv('df_bseid_qtrid.csv')
logging.info("bseid has been quried successfully")
bseticker=list(df_bseid_qtrid['BSETicker'])
logging.info(f"bseid has length of {len(bseticker)}")
period_id=[89,93,97,100,101,102]


if __name__=='__main__':
    try:
        for bseid in bseticker:
            logging.info(f"{bseid} has started")
            for qtrid in period_id:
                URL=f'https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd={str(bseid)}&qtrid={str(qtrid)}'
                logging.info(f"{URL}")
                try:
                    obj1=PromoterNGroup(URL)
                    if obj1.check_availability==False:
                        continue
                    logging.debug(f"{obj1.get_column_name(self,tree)}")
                    df=obj1.col_having_six()
                    #set_trace()
                    logging.info(f"df PromoterNGroup has {bseid} and {qtrid} been created ")
                    #sql_obj.append_db(df,conn=tmp_table_conn,tabl_name="tmp_tbl_company",schema='tmp')
                except (ValueError,Exception) as v:
                    logging.info(f"{format_exc()}")
                    obj2=PromoterNGroupVariation(URL)
                    if obj2.check_availability==False:
                        continue
                    df=obj2.col_having_six()
                    logging.info(f"In Exception df PromoterNGroupVariation has {bseid} and {qtrid} been created ")
                    #sql_obj.append_db(df,conn=tmp_table_conn,tabl_name="tmp_tbl_company_extracols",schema='tmp')
            logging.info(f"{bseid} and {qtrid} has finished")
    except Exception as e:
        logging.info(f"Finally the exception is {format_exc()}")