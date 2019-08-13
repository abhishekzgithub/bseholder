def get_column_name(tree):
    cols=tree.find_class('innertable_header1')
    cols=[cols[i].text_content().encode('ascii', 'ignore').decode("utf-8") for i in range(len(cols))]
    return cols

import re
def get_data(tree):
    all_cols=tree.find_class('TTRow_right')
    all_cols=[re.sub(r"[\s+|,]", "", i.text_content()) for i in all_cols]
    return all_cols

def get_right_column_data(tree):
    cols=tree.find_class('TTRow_left')
    cols=[(cols[i].text_content()).encode('ascii', 'ignore').decode("utf-8") for i in range(len(cols))]
    return cols


def fit_data(tree,cols,df):
    datum=get_data(tree)
    print(cols)
    j=1
    for i in range(0,len(datum),5):
        print(i,datum[i:i+5])

def col_having_six(URL):
    r = requests.get(URL)
    tree = html.fromstring(r.content)
    cols=get_column_name(tree)
    df=pd.DataFrame(columns=cols)
    df[cols[0]]=get_right_column_data(tree)
    df=fit_data(tree,cols,df)
    return df