import requests
import pandas as pd
from lxml import html
import re
def get_extra_col_df(cols):
    for ix,val in enumerate(cols):
        if ix==5:
            df[cols[ix]+'-'+cols[-2]]=" "
            df[cols[ix]+'-'+cols[-1]]=" "
            continue
        elif ix>=7:
            pass
        else:
            df[val]=" "
    return df
class PromoternGroup(object):
    def get_column_name(self,tree):
        cols=tree.find_class('innertable_header1')
        cols=[cols[i].text_content().encode('ascii', 'ignore').decode("utf-8") for i in range(len(cols))]
        return cols
    
    def get_data(self,tree):
        all_cols=tree.find_class('TTRow_right')
        all_cols=[re.sub(r"[\s+|,]", "", i.text_content()) for i in all_cols]
        return all_cols
    
    def get_right_column_data(self,tree):
        cols=tree.find_class('TTRow_left')
        cols=[(cols[i].text_content()).encode('ascii', 'ignore').decode("utf-8") for i in range(len(cols))]
        return cols
    
    def fit_data(self,tree,cols,df):
        datum=self.get_data(tree)
        print(cols)
        data={}
        j=1
        for i in range(0,len(datum),len(cols)-1):
            data[j]=(datum[i:i+5])
            j+=1
        df1=pd.DataFrame(data).T
        df1.columns=cols[1:]
        return df1
    
    def col_having_six(self,URL):
        r = requests.get(URL)
        tree = html.fromstring(r.content)
        cols=self.get_column_name(tree)
        df=pd.DataFrame()
        df=(self.fit_data(tree,cols,df))
        df[cols[0]]=self.get_right_column_data(tree)
        return df.replace(r'^\s*$', 0, regex=True)

