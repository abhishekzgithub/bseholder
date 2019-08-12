import requests
import pandas as pd
from lxml import html

def get_table_df():
    try:
        URL=r'https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd=532500&qtrid=102.00&QtrName=June%202019'
        #URL=r'https://www.bseindia.com/corporates/shpPublicShareholder.aspx?scripcd=532500&qtrid=101.00&QtrName=June%202019'
        r = requests.get(URL)
        tree = html.fromstring(r.content)
        cols=tree.xpath('//*[@class="innertable_header1"]/text()')
        df=pd.DataFrame(columns=cols)
        for i in range(0,len(cols)):
            tr_elements=tree.xpath(f'//tr[3]//td[{i+1}]')
            if i==0:
                df[cols[i]]=[(T.text_content()) for T in tr_elements][-7:]
            #print(tr_elements)
            else:
                df[cols[i]]=[(T.text_content()) for T in tr_elements]
    except ValueError:
        print(i)
        print(ValueError)
    return df.iloc[1:,:]
get_table_df()