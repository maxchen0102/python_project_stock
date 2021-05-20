

from datetime import datetime
import twstock
import sqlite3

conn=sqlite3.connect('StockTest01.db')
c=conn.cursor()

stock = twstock.Stock('2330')
test=list(stock.fetch(2021,5))
day=[0,0,0,0,0]

for l in range(5):
    d=datetime.strftime(test[l][0],'%Y%m%d')
    day[l]=int(d)

c.execute('DROP table if exists stocktest')
c.execute('CREATE TABLE stocktest( date INTEGER, capacity INTEGER, turnover INTEGER, open REAL, high REAL, low REAL, close REAL, change REAL, transactions INTEGER)')

for row in range(5):
    c.execute("INSERT INTO stocktest VALUES ({},{},{},{},{},{},{},{},{})".format(day[row],test[row][1],test[row][2],test[row][3],test[row][4],test[row][5],test[row][6],test[row][7],test[row][8]))


print(test[row][1])
conn.commit()
conn.close()

