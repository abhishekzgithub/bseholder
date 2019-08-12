import requests
import bs4
URL=r'https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd=532500&qtrid=102.00&QtrName=June%202019'
r = requests.get(URL)
soup = bs4.BeautifulSoup(r.content, 'html5lib') 
print(soup.prettify())

