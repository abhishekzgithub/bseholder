from main import PublicShareholder_df,get_table_promoter_n_group_df
bse_ticker=[540710,
531624,
540776,
532682,
'ABMINTLTD',
538365,
532727,
540691,
539056,
531921,
500463,
532806,
532351,
524075,
526707,
532875,
530715,
531400,
521070,
520077,
530721]


BSETicker=str(1003)
period_id=100.00
URL=f'https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd={BSETicker}&qtrid={period_id}&QtrName=June%202019'
URL='https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd=519353&qtrid=101.00&QtrName=March%202019'
URL='https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd=513151&qtrid=102.00&QtrName=June%202019'
df=get_table_promoter_n_group_df(URL)
#df.to_csv("scraped.csv")
print(df.head())