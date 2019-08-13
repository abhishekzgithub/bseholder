def PublicShareholder_df(URL):
    try:
        #URL=r'https://www.bseindia.com/corporates/shpPublicShareholder.aspx?scripcd=532500&qtrid=101.00&QtrName=June%202019'
        r = requests.get(URL)
        tree = html.fromstring(r.content)
        cols=tree.xpath('//*[@class="innertable_header1"]/text()')
        df=pd.DataFrame(columns=cols)
        for i in range(0,len(cols)):
            try:
                tr_elements=tree.xpath(f'//tr[3]//td[{i+2}]')
                if i==2:
                    df[cols[i]]=[(T.text_content()) for T in tr_elements][2:]
                elif i+2==5:
                    df[cols[i]]=[tree.xpath(f'//tr[{i}]//td[7]')[0].text_content() for i in range(7,df.shape[0]-1+7+1)]
                elif i+2==6:
                    df[cols[i]]=[tree.xpath(f'//tr[{i}]//td[8]')[0].text_content() for i in range(7,df.shape[0]-1+7+1)]
                elif i+2 in (7,8) :
                    df[cols[i]]=[(T.text_content()) for T in tr_elements][1:]
                elif i+2==9:
                    df[cols[i]]=[tree.xpath(f'//tr[{i}]//td[19]')[0].text_content() for i in range(7,df.shape[0]-1+7+1)]
                else:
                    df[cols[i]]=[(T.text_content()) for T in tr_elements][3:]
            except Exception:
                print(Exception)
                print(i+2)
                continue
    except ValueError:
        print(ValueError)
        print(i)
    return df.replace(r'^\s*$', 0, regex=True)

