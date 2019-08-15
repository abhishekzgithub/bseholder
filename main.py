import requests
import pandas as pd
from lxml import html
import re
from pdb import set_trace

class PromoterNGroup(object):
    def __init__(self,URL):
        self.URL=URL
        self.r = requests.get(self.URL)
        self.tree = html.fromstring(self.r.content)
    def check_availability(self):
        status=True
        #r = requests.get(self.URL)
        r_status=self.r.status_code
        tree = html.fromstring(self.r.content)
        empty=(tree.xpath("//td[contains(text(),'Category of shareholder')]/text()"))
        if r_status in (404,'404') and empty=='Category of shareholder':
            status=False
        return status
    def get_column_name(self):
        cols=self.tree.find_class('innertable_header1')
        cols=[cols[i].text_content().encode('ascii', 'ignore').decode("utf-8") for i in range(len(cols))]
        return cols
    
    def get_data(self):
        all_cols=self.tree.find_class('TTRow_right')
        all_cols=[re.sub(r"[\s+|,]", "", i.text_content()) for i in all_cols]
        return all_cols
    
    def get_right_column_data(self):
        cols=self.tree.find_class('TTRow_left')
        cols=[(cols[i].text_content()).encode('ascii', 'ignore').decode("utf-8") for i in range(len(cols))]
        return cols
    
    def fit_data(self,cols):
        datum=self.get_data()
        data={}
        j=1
        for i in range(0,len(datum),len(cols)-1):
            data[j]=(datum[i:i+5])
            j+=1
        df1=pd.DataFrame(data).T
        df1.columns=cols[1:]
        return df1
    
    def col_having_six(self):
        cols=self.get_column_name()
        df=pd.DataFrame()
        df=self.fit_data(cols)
        df[cols[0]]=self.get_right_column_data()
        return df.replace(r'^\s*$', 0, regex=True)

class PromoterNGroupVariation(PromoterNGroup):
    def __init__(self,URL):
        self.URL=URL
        self.r = requests.get(self.URL)
        self.tree = html.fromstring(self.r.content)

    def get_extra_col_df(self,cols):
        df=pd.DataFrame()
        for ix,val in enumerate(cols):
            if ix==5:
                df[cols[ix]+'->'+cols[-2]]=" "
                df[cols[ix]+'->'+cols[-1]]=" "
                continue
            elif ix>=7:
                pass
            else:
                df[val]=" "
        return list(df.columns[1:])

    def fit_data(self,cols):
        datum=self.get_data()
        data={}
        j=1
        for i in range(0,len(datum),7):
            data[j]=datum[i:i+7]
            j+=1
        df1=pd.DataFrame(data).T
        df1.columns=self.get_extra_col_df(cols)
        return df1

class PromoterNGroupVariation7Cols(PromoterNGroup):
    #todo
    def __init__(self,URL):
        self.URL=URL
        self.r = requests.get(self.URL)
        self.tree = html.fromstring(self.r.content)

    def get_extra_col_df(self,cols):
        df=pd.DataFrame()
        for ix,val in enumerate(cols):
            if ix==5:
                df[cols[ix]+'->'+cols[-2]]=" "
                df[cols[ix]+'->'+cols[-1]]=" "
                continue
            elif ix>=7:
                pass
            else:
                df[val]=" "
        return list(df.columns[1:])

    def fit_data(self,cols):
        datum=self.get_data()
        data={}
        j=1
        for i in range(0,len(datum),7):
            data[j]=datum[i:i+7]
            j+=1
        df1=pd.DataFrame(data).T
        df1.columns=self.get_extra_col_df(cols)
        return df1

# if __name__=='__main__':
#     try:
#         URL=''
#         obj1=PromoterNGroup(URL)
#         df=obj1.col_having_six()
#     except ValueError as v:
#         obj1=PromoterNGroupVariation(URL)
#         df=obj1.col_having_six()
        
