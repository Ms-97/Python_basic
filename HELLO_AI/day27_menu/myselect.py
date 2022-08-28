import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='python', port=3305,
                       db='python', charset='utf8')
 
curs = conn.cursor()

sql = "select menu from menu WHERE e_id='2'"
curs.execute(sql)
 

rows = curs.fetchall()
print(rows)     

curs.close()
conn.close()
