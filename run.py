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
bsetickerid=list(df_bseid_qtrid['BSETicker'])
logging.info(f"bseid has length of {len(bsetickerid)}")
period_id=[89,93,97,100,101,102]

def main(obj,**kwargs):
    df=obj.col_having_six()
    logging.info(f"In Exception df PromoterNGroupVariation has {bseid} and {qtrid} been created ")
    #sql_obj.append_db(df,conn=tmp_table_conn,tabl_name="tmp_tbl_company_extracols",schema='tmp')
    return df

def init(bseticker=[]):
    try:
        tup=tuple()
        dic=dict()
        col_uniq=set()
        for bseid in bseticker:
            logging.info(f"{bseid} has started")
            for qtrid in period_id:
                URL=f'https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd={str(bseid)}&qtrid={str(qtrid)}'
                logging.info(f"{URL}")
                try:
                    obj1=PromoterNGroup(URL)
                    if obj1.check_availability==False:
                        continue
                    val=obj1.get_column_name()
                    dic[tuple(val)]=URL
                    col_uniq.update(set(val))
                    #continue
                    logging.info(f"{obj1.get_column_name()}")
                    result=main(obj1)
                    logging.info(f"df PromoterNGroup has {bseid} and {qtrid} been created ")
                except IndexError as ie:
                    logging.info(f"exception in PromoterNGroup having {bseid} and {qtrid} has  index error and thus continue ")
                    logging.info(f"{ie}{format_exc()}")
                    continue
                except (ValueError,Exception) as v:
                    #logging.info(f"{format_exc()}")
                    try:
                        obj2=PromoterNGroupVariation(URL)
                        if obj2.check_availability==False:
                            continue
                        #logging.info(f"{obj2.get_column_name()}")
                        result=main(obj2)
                        logging.info(f"In Exception df PromoterNGroupVariation has {bseid} and {qtrid} been created ")
                    except ValueError as v:
                        try:
                            obj3=PromoterNGroupVariation7Cols(URL)
                            if obj3.check_availability==False:
                                continue
                            #logging.info(f"{obj3.get_column_name()}")
                            result=main(obj3)
                            logging.info(f"In Exception df PromoterNGroupVariation7Cols has {bseid} and {qtrid} been created ")
                        except ValueError as v:
                            try:
                                obj4=PromoterNGroupVariation9Cols(URL)
                                if obj4.check_availability==False:
                                    continue
                                #logging.info(f"{obj4.get_column_name()}")
                                result=main(obj4)
                                logging.info(f"In Exception df PromoterNGroupVariation9Cols has {bseid} and {qtrid} been created ")
                            except ValueError as v:
                                try:
                                    obj4=PromoterNGroupVariation11Cols(URL)
                                    if obj4.check_availability==False:
                                        continue
                                    #logging.info(f"{obj4.get_column_name()}")
                                    result=main(obj4)
                                    logging.info(f"In Exception df PromoterNGroupVariation11Cols has {bseid} and {qtrid} been created ")
                                except ValueError as v:
                                    try:
                                        obj4=PromoterNGroupVariation12Cols(URL)
                                        if obj4.check_availability==False:
                                            continue
                                        #logging.info(f"{obj4.get_column_name()}")
                                        result=main(obj4)
                                        logging.info(f"In Exception df PromoterNGroupVariation12Cols has {bseid} and {qtrid} been created ")
                                    except ValueError as v:
                                        try:
                                            obj4=PromoterNGroupVariation13Cols(URL)
                                            if obj4.check_availability==False:
                                                continue
                                            #logging.info(f"{obj4.get_column_name()}")
                                            result=main(obj4)
                                            logging.info(f"In Exception df PromoterNGroupVariation13Cols has {bseid} and {qtrid} been created ")
                                        except ValueError as v:
                                            try:
                                                obj4=PromoterNGroupVariation17Cols(URL)
                                                if obj4.check_availability==False:
                                                    continue
                                                #logging.info(f"{obj4.get_column_name()}")
                                                result=main(obj4)
                                                logging.info(f"In Exception df PromoterNGroupVariation13Cols has {bseid} and {qtrid} been created ")
                                            except ValueError as v:
                                                print(v)
                                                logging.info(f"Unhandled the exception in {URL}")
                                                logging.info(f"the exception is {format_exc()}")

            logging.info(f"{bseid} and {qtrid} has finished")
    except Exception as e:
        logging.info(f"Finally the exception is {format_exc()}")
    finally:
        logging.info("list of columns as"+"\n"+f"{dic}")
        logging.info(f"The unique columns are {col_uniq} ")

if __name__=='__main__':
    init(bseticker=bsetickerid)