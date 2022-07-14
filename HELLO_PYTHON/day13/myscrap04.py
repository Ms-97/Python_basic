import requests
from bs4 import BeautifulSoup
import datetime
from day13.daostock import DaoStock



ds = DaoStock()

now = datetime.datetime.now()
ymd = now.strftime("%Y%m%d.%H%M")

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"

html = requests.get(url)
html.encoding='EUC-KR'


soup = BeautifulSoup(html.text, 'html.parser')
tds = soup.find_all("td","st2")

for td in tds:
    s_name = td.text
    s_code = td.a['title']
    price = td.parent.find_all("td")[1].text.replace(",","")
    cnt = ds.insert(s_code, ymd, s_name, price)
    print("cnt",cnt)  

