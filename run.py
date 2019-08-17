import requests
from lxml import html
import logging
from traceback import format_exc
from pdb import set_trace

from main import *
from extended_main import *
from db_utlity import *
from utility import *
import constants

logging.basicConfig(filename='output.log',filemode='w',level=logging.INFO,format=constants.LOG_FORMAT)

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

columns_type_df=pd.read_csv("unique_type_columns.csv")

def save_df(df,tabl_name="tmp_tbl_company_extracols",local_save=True,caseid="",filename=""):
    if not local_save:
        sql_obj.append_db(df,conn=tmp_table_conn,tabl_name=tabl_name,schema='tmp')
    else:
        df.to_csv(str(filename)+".csv",index=False)

def init(bseticker=[]):
    try:
        for bseid in bseticker:
            logging.info(f"{bseid} has started")
            for qtrid in period_id:
                URL=f'https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd={str(bseid)}&qtrid={str(qtrid)}'
                logging.info(f"{URL}")
                try:
                    r = requests.get(URL)
                    if not available(r):
                        continue
                    tree = html.fromstring(r.content)
                    columns,status=get_column_name(tree)
                    if not status and columns==[]:
                        continue
                    case_type=int(list(df2[df2.cols==columns].case)[0])
                    if case_type==1:
                        df=Case1(tree).final_result()
                    elif case_type==2:
                        df=Case2(tree).final_result()
                    elif case_type==3:
                        df=Case3(tree).final_result()
                    elif case_type==4:
                        df=Case4(tree).final_result()
                    elif case_type==5:
                        df=Case5(tree).final_result()
                    elif case_type==6:
                        df=Case6(tree).final_result()
                    elif case_type==7:
                        df=Case7(tree).final_result()
                    elif case_type==8:
                        df=Case8(tree).final_result()
                    elif case_type==9:
                        df=Case9(tree).final_result()
                    elif case_type==10:
                        df=Case10(tree).final_result()
                    save_df(df,filename=str(bseid)+str(qtrid))
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)

if __name__=='__main__':
    print("Program has started")
    #init(bseticker=bsetickerid)