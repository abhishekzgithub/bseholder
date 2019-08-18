import requests
from lxml import html
import logging
from traceback import format_exc
from pdb import set_trace
import os

from main import *
from extended_main import *
from db_utlity import *
from utility import *
import constants
from datetime import datetime
dt_time=datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

logging.basicConfig(filename=f'{dt_time}_output.log',filemode='w',level=logging.INFO,format=constants.LOG_FORMAT)
SCRAPED_DATA=os.path.join(os.getcwd(),"scraped_data")


#get the bseticker id from the database
# sql_obj=SQlAlchemyOperation()
# tmp_table_conn=sql_obj.get_sqlalchemy_conn(database_name="tmp")
# pymysql_obj=MysqlConn()
# conn=pymysql_obj.pymysql_connect()
# df_bseid_qtrid=pymysql_obj.pymysql_get_dataframe(query=constants.q,conn=conn)
# df_bseid_qtrid.to_csv("df_bseid_qtrid.csv",index=False)

df_bseid_qtrid=pd.read_csv('df_bseid_qtrid.csv')
logging.info("bseid has been quried successfully")
bsetickerid=list(df_bseid_qtrid['BSETicker'])
logging.info(f"bseid has length of {len(bsetickerid)}")

columns_type_df=pd.read_csv("unique_type_columns.csv")


def save_df(df,tabl_name="tmp_tbl_company_extracols",local_save=True,caseid="",filename="",action="fail"):
    if not local_save:
        sql_obj.append_db(df,conn=tmp_table_conn,tabl_name=tabl_name,schema='tmp',action=action)
    else:
        df.to_csv(os.path.join(os.getcwd(),"scraped_data",str(filename)+str(dt_time)+".csv"),index=False)

def init(bseticker=[]):
    final_df=pd.DataFrame()
    url_exeception=[]
    try:
        for bseid in bseticker:
            logging.info(f"{bseid} has started")
            for qtrid in constants.period_id:
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
                    case_type=int(list(columns_type_df[columns_type_df.cols==str(tuple(columns))].case)[0])
                    if case_type==1:
                        df=Case1(tree,columns).final_result()
                    elif case_type==2:
                        df=Case2(tree,columns).final_result()
                    elif case_type==3:
                        df=Case2(tree,columns).final_result()
                    elif case_type==4:
                        df=Case3(tree,columns).final_result()
                    elif case_type==5:
                        df=Case4(tree,columns).final_result()
                    elif case_type==6:
                        df=Case5(tree,columns).final_result()
                    elif case_type==7:
                        df=Case4(tree,columns).final_result()
                    elif case_type==8:
                        df=Case6(tree,columns).final_result()
                    elif case_type==9:
                        df=Case7(tree,columns).final_result()
                    elif case_type==10:
                        df=Case8(tree,columns).final_result()
                    elif case_type==10:
                        df=Case8(tree,columns).final_result()                        
                    elif case_type==11:
                        df=Case1(tree,columns).final_result()
                    elif case_type==12:
                        df=Case9(tree,columns).final_result()
                    elif case_type==13:
                        df=Case10(tree,columns).final_result()
                    elif case_type==14:
                        df=Case1(tree,columns).final_result()
                    elif case_type==15:
                        df=Case2(tree,columns).final_result()
                    elif case_type==16:
                        df=Case2(tree,columns).final_result()
                    elif case_type==17:
                        df=Case3(tree,columns).final_result()
                    elif case_type==18:
                        df=Case1(tree,columns).final_result()
                    elif case_type==19:
                        df=Case11(tree,columns).final_result()
                    elif case_type==20:
                        df=Case11(tree,columns).final_result()
                    elif case_type==21:
                        df=Case12(tree,columns).final_result()
                    elif case_type==22:
                        df=Case1(tree,columns).final_result()
                    elif case_type==23:
                        df=Case9(tree,columns).final_result()
                    elif case_type==24:
                        df=Case9(tree,columns).final_result()
                    elif case_type==25:
                        df=Case10(tree,columns).final_result()
                    elif case_type==26:
                        df=Case13(tree,columns).final_result()
                    elif case_type==27:
                        df=Case14(tree,columns).final_result()
                    elif case_type==28:
                        df=Case15(tree,columns).final_result()
                    elif case_type==29:
                        df=Case16(tree,columns).final_result()
                    elif case_type==30:
                        df=Case17(tree,columns).final_result()
                    elif case_type==31:
                        df=Case18(tree,columns).final_result()
                    elif case_type==32:
                        df=Case18(tree,columns).final_result()
                    elif case_type==33:
                        df=Case10(tree,columns).final_result()
                    elif case_type==34:
                        df=Case1(tree,columns).final_result()
                    elif case_type==35:
                        df=Case2(tree,columns).final_result()
                    elif case_type==36:
                        df=Case2(tree,columns).final_result()
                    elif case_type==37:
                        df=Case3(tree,columns).final_result()                    
                    elif case_type==38:
                        df=Case17(tree,columns).final_result()
                    elif case_type==39:
                        df=Case1(tree,columns).final_result()
                    elif case_type==40:
                        df=Case2(tree,columns).final_result()
                    elif case_type==41:
                        df=Case2(tree,columns).final_result()
                    elif case_type==42:
                        df=Case3(tree,columns).final_result()
                    elif case_type==43:
                        df=Case17(tree,columns).final_result()
                    elif case_type==44:
                        df=Case19(tree,columns).final_result()
                    elif case_type==45:
                        df=Case20(tree,columns).final_result()
                    elif case_type==46:
                        df=Case9(tree,columns).final_result()
                    df['bseid']=bseid
                    df['qtrid']=qtrid
                    final_df=pd.concat([final_df,df],ignore_index=True)
                except Exception as e:
                    print("In Exception inner",e,case_type,URL,sep="\n")
                    url_exeception.append(URL)
                    logging.info(f"{e}{format_exc()} \n caseid is {case_type} \n {URL}")

    except Exception as e:
        print(e)
        url_exeception.append(URL)
        logging.info(f"{e} \n {format_exc()}{URL}")
    finally:
        logging.info(f"exceptional urls are {url_exeception}")
        save_df(final_df,filename="final_df")
if __name__=='__main__':
    print("Program has started")
    #init(bseticker=bsetickerid)
    # df=pd.read_csv(SCRAPED_DATA+"/final_df.csv")
    # print(df.shape)
    #save_df(df,tabl_name="tmp_tbl_company_extracols",local_save=False,action="replace")
