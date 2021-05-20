

import pandas as pd 


from datetime import datetime
import twstock
from twstock import Stock 
import time 
from tqdm import tqdm 

stock=Stock("2330")
time.sleep(2); # 延遲兩秒 

stock.fetch(2010, 4) 


date=stock.date #日期
high_price=stock.high #盤中最高價
low_price=stock.low # 盤中最低價
close_price=stock.close #收盤價 
open_price= stock.open # 開盤價 
capacity=stock.capacity # 總成總成交股數 
turnover=stock.turnover # 總成交金額 
change= stock.change # 漲跌價差 
transaction= stock.transaction # 成交筆數 

day_number= len(date)

# 建立 和天數相符的 [0] list
day_list=[]
day_list=[0]*day_number
#把取出的time 轉乘int 再存入day_list  
for i in tqdm(range(day_number)):
    tem=datetime.strftime(date[i],'%Y%m%d')
    day_list[i]=int(tem)


#把各個資料建立list 
high_price_list=[]
low_price_list=[]
close_price_list=[] 
open_price_list=[]
capacity_list=[] 
turnover_list=[]
change_list=[]
transaction_list=[]


# 把各個資料存入list 
high_price_list=high_price
low_price_list=low_price
close_price_list=close_price
open_price_list=open_price
capacity_list=capacity
turnover_list=turnover
change_list=change
transaction_list=transaction


print(close_price_list[1])

import sqlite3
con = sqlite3.connect('MyTest.db')

# 會自己幫我建立 .db檔案

cur = con.cursor()
# Create tabl


cur.execute('CREATE TABLE test( 標籤 INTEGER,日期 INTEGER,盤中最低價 INTEGER, 盤中最高價 INTEGER,收盤價 INTEGER,開盤價 INTEGER \
         總成總成交股數 INTEGER,總成交金額 INTEGER,漲跌價差 INTEGER, 成交筆數 INTEGER)')

# Insert a row of data

for i in tqdm(range(day_number)) :
    cur.execute("INSERT INTO test VALUES ({},{},{},{},{},{},{},{},{})".format(i+1,day_list[i],low_price_list[i],high_price_list[i],close_price_list[i]\
,open_price[i],capacity[i],turnover[i],change_list[i],transaction_list[i]))
          

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()




print("done")
        
''' 
dict = {"日期": date, 
        "收盤價": close_price ,
        "開盤價":open_price ,
        "盤中最高價":high_price,
        "盤中最低價":low_price,
        "總成總成交股數 ":capacity,
        "總成交金額":turnover, 
        "漲跌價差":change, 
        "成交筆數": transaction, 
        }
''' 


''' 

df = pd.DataFrame(dict)


df.index=[i+1 for i in range(len(stock.date))]

## df.columns=["日期","收盤價","開盤價","盤中最高價","盤中最低價","總成總成交股數","總成交金額","漲跌價差","成交筆數"]
df.style.set_properties(**{'text-align': 'right'})


print("=============================")
print("ID:",end="")
print(stock.sid )
print("=============================")


for i in range(len(stock.date)):
        print(df[i:i+1])

print("=============================")

''' 


''' 
import sqlite3
con = sqlite3.connect('MyTest.db')

# 會自己幫我建立 .db檔案 

cur = con.cursor()
# Create tabl


cur.execute('CREATE TABLE stocktest(date INTEGER, capacity INTEGER, turnover INTEGER, open REAL, high REAL, low REAL, close REAL, change REAL, transactions INTEGER)')


# Insert a row of data

cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")


# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()



print("done")

''' 