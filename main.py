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
        cols=[i.text_content().encode('ascii', 'ignore').decode("utf-8") for i in (cols)]
        return cols
    
    def get_data(self):
        all_cols=self.tree.find_class('TTRow_right')
        all_cols=[re.sub(r"[\s+|,]", "", i.text_content()) for i in all_cols]
        return all_cols
    
    def get_right_column_data(self):
        righ_data_xpath=self.tree.find_class('TTRow_left')
        right_data=[(i.text_content()).encode('ascii', 'ignore').decode("utf-8") for i in (righ_data_xpath)]
        return right_data
    
    def set_data(self):
        datum=self.get_data()
        firstcols=self.get_right_column_data()
        data={}
        j=1
        matrix_size=int(len(datum)/len(firstcols))
        for i in range(0,len(datum),matrix_size):
            data[j]=datum[i:i+matrix_size]
            j+=1
        df=pd.DataFrame(data).T
        df.insert(0,"Category of shareholder",self.get_right_column_data())
        return df
    
    def set_column_name(self):
        col_name=self.get_column_name()
        return col_name
    
    def final_result(self):
        df=self.set_data()
        df.columns=self.set_column_name()
        return df.replace(r'^\s*$', 0, regex=True)


# if __name__=='__main__':
#     try:
#         URL=''
#         obj1=PromoterNGroup(URL)
#         df=obj1.col_having_six()
#     except ValueError as v:
#         obj1=PromoterNGroupVariation(URL)
#         df=obj1.col_having_six()
        
