import pandas as pd
def available(r):
    status=True
    r_status=r.status_code
    if r_status in (404,'404'):
        status=False
    return status

def get_column_name(tree):
    try:
        status=True
        cols_element=tree.find_class('innertable_header1')
        cols=[i.text_content().encode('ascii', 'ignore').decode("utf-8") for i in (cols_element)]
    except Exception:
        cols=[]
        status=False 
    return cols,status

def update_unique_type_columns_csv(col_dict_urls):
    df2=pd.DataFrame(list(col_dict_urls.items()),columns=['cols', 'urls'])
    df2.sort_values(by='cols',ascending=False,inplace=True)
    df2.reset_index(drop=True,inplace=True)
    df2['case']=df2.index
    #df2.to_csv("unique_type_columns.csv",index=False)    