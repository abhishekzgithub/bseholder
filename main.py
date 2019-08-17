import requests
import pandas as pd
from lxml import html
import re
from pdb import set_trace
class PromoterNGroup(object):
    def __init__(self,tree):
        self.tree = tree
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
    
    def fit_data(self):
        datum=self.get_data()
        firstcols=self.get_right_column_data()
        data={}
        j=1
        matrix_size=int(len(datum)/len(firstcols))
        for i in range(0,len(datum),matrix_size):
            data[j]=datum[i:i+matrix_size]
            j+=1
        df1=pd.DataFrame(data).T
        return df1
    def set_column_name(self):
        pass

    
    def final_result(self):
        df=self.fit_data()
        df.columns=self.set_column_name()
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
    """
    e.g. URL='https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd=500124&qtrid=89'
    this has 6 columns excluding the category ones
    """
    def __init__(self,URL):
        self.URL=URL
        self.r = requests.get(self.URL)
        self.tree = html.fromstring(self.r.content)

    def fit_data(self,cols):
        datum=self.get_data()
        data={}
        j=1
        for i in range(0,len(datum),6):
            data[j]=datum[i:i+6]
            j+=1
        df1=pd.DataFrame(data).T
        df1.columns=(self.get_column_name())[1:]
        return df1

"""
Length mismatch: Expected axis has 5 elements, new values have 9 elements
"""
class PromoterNGroupVariation9Cols(PromoterNGroup):
    """
    e.g. URL='https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd=500124&qtrid=89'
    this has 6 columns excluding the category ones
    """
    def __init__(self,URL):
        self.URL=URL
        self.r = requests.get(self.URL)
        self.tree = html.fromstring(self.r.content)
    
    def get_extra_col_df(self,cols):
        df=pd.DataFrame()
        for ix,val in enumerate(cols):
            if ix==6:
                df[cols[ix]+'->'+cols[-2]]=" "
                df[cols[ix]+'->'+cols[-1]]=" "
                continue
            elif ix>=8:
                pass
            else:
                df[val]=" "
        return list(df.columns[1:])    


    def fit_data(self,cols):
        datum=self.get_data()
        data={}
        j=1
        for i in range(0,len(datum),8):
            data[j]=datum[i:i+8]
            j+=1
        df1=pd.DataFrame(data).T
        df1.columns=self.get_extra_col_df(cols)
        return df1
"""
ValueError: Length mismatch: Expected axis has 5 elements, new values have 11 elements
"""
class PromoterNGroupVariation11Cols(PromoterNGroup):
    """
    e.g. URL='https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd=533022&qtrid=89'
    this has 9 columns excluding the category ones
    """
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
            if ix==6:
                df[cols[ix]+'->'+cols[-2]]=" "
                df[cols[ix]+'->'+cols[-1]]=" "
                continue
            elif ix>=8:
                pass
            else:
                df[val]=" "
        return list(df.columns[1:])    


    def fit_data(self,cols):
        datum=self.get_data()
        data={}
        j=1
        for i in range(0,len(datum),9):
            data[j]=datum[i:i+9]
            j+=1
        df1=pd.DataFrame(data).T
        df1.columns=self.get_extra_col_df(cols)
        return df1

"""
ValueError: Length mismatch: Expected axis has 5 elements, new values have 12 elements
"""        
class PromoterNGroupVariation12Cols(PromoterNGroup):
    """
    e.g. URL='https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd=533292&qtrid=89'
    """
    def __init__(self,URL):
        self.URL=URL
        self.r = requests.get(self.URL)
        self.tree = html.fromstring(self.r.content)
    
    def get_extra_col_df(self,cols):
        df=pd.DataFrame()
        for ix,val in enumerate(cols):
            if ix==6:
                df[cols[ix]+'->'+cols[-2]]=" "
                df[cols[ix]+'->'+cols[-1]]=" "
                continue
            if ix==7:
                df[cols[ix]+'->'+cols[-2]]=" "
                df[cols[ix]+'->'+cols[-1]]=" "
                continue
            elif ix>8:
                pass
            else:
                df[val]=" "
        return list(df.columns[1:])    


    def fit_data(self,cols):
        datum=self.get_data()
        data={}
        j=1
        for i in range(0,len(datum),10):
            data[j]=datum[i:i+10]
            j+=1
        df1=pd.DataFrame(data).T
        df1.columns=self.get_extra_col_df(cols)
        return df1

"""
ValueError: Length mismatch: Expected axis has 5 elements, new values have 13 elements
"""        
class PromoterNGroupVariation13Cols(PromoterNGroup):
    """
    e.g. URL='https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd=506074&qtrid=97'
    """
    def __init__(self,URL):
        self.URL=URL
        self.r = requests.get(self.URL)
        self.tree = html.fromstring(self.r.content)
    
    def get_extra_col_df(self,cols):
        df=pd.DataFrame()
        for ix,val in enumerate(cols):
            if ix==7:
                df[cols[ix]+'->'+cols[-2]]=" "
                df[cols[ix]+'->'+cols[-1]]=" "
                continue
            if ix==8:
                df[cols[ix]+'->'+cols[-2]]=" "
                df[cols[ix]+'->'+cols[-1]]=" "
                continue
            elif ix>9:
                pass
            else:
                df[val]=" "
        return list(df.columns[1:])    


    def fit_data(self,cols):
        datum=self.get_data()
        data={}
        j=1
        for i in range(0,len(datum),11):
            data[j]=datum[i:i+11]
            j+=1
        df1=pd.DataFrame(data).T
        df1.columns=self.get_extra_col_df(cols)
        return df1

"""
ValueError: Length mismatch: Expected axis has 5 elements, new values have 17 elements
"""
class PromoterNGroupVariation17Cols(PromoterNGroup):
    """
    e.g. URL='https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd=532759&qtrid=93'
    """
    def __init__(self,URL):
        self.URL=URL
        self.r = requests.get(self.URL)
        self.tree = html.fromstring(self.r.content)
    
    def get_extra_col_df(self,cols):
        df=pd.DataFrame()
        for ix,val in enumerate(cols):
            if ix==5:
                df[cols[ix]+'->'+cols[15]]=" "
                df[cols[ix]+'->'+cols[16]]=" "
                df[cols[ix]+'->'+cols[10]]=" "
                df[cols[ix]+'->'+cols[17]]=" "
                continue
            if ix==6:
                df[cols[ix]+'->'+cols[11]]=" "
                df[cols[ix]+'->'+cols[12]]=" "
                continue
            if ix==7:
                df[cols[ix]+'->'+cols[13]]=" "
                df[cols[ix]+'->'+cols[14]]=" "
            elif ix>8:
                pass
            else:
                df[val]=" "
        return list(df.columns[1:])    


    def fit_data(self,cols):
        datum=self.get_data()
        firstcols=self.get_right_column_data()
        data={}
        j=1
        matrix_size=int(len(datum)/len(firstcols))
        for i in range(0,len(datum),matrix_size):
            data[j]=datum[i:i+matrix_size]
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
        
