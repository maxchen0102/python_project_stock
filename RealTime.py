

#=================
#即時查詢系統 
#================
import twstock 
from twstock import Stock 
from twstock import realtime


#輸入你要查詢的股票代號 
stock_number=input("enter your stock number ") 



#得到所有當日即時資訊 包含一個為info的字典 在原字典中

stock_info=twstock.realtime.get(stock_number) 



#把字典裡面的字典取出來d
info=stock_info['info']


print("查詢時間",info['time'])
print("股票代號",info['code'])
print("股票名稱",info['name'])
print("股票全名",info['fullname'])




print("最佳買入價",stock_info['best_bid_price'])
print("最佳買入數量",stock_info['best_bid_volume'])

print("最佳賣出價",stock_info['best_bid_volume'])
print("最佳賣出數量",stock_info['best_ask_price'])


print("開盤價",stock_info['open'])
print("最高價",stock_info['high'])
print("最低價",stock_info['low'])





''' 
查詢時間、股票代號、股票名稱、股名票全
 最佳買入價(best bid price)、最佳買入數量(best bid volume)
 最佳賣出價(best ask price)、最佳賣出數量(best ask volume) 
 開盤價、最高價、最低價
'''
