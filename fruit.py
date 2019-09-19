# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:53:27 2019
program: fruit
author: Paul
Date: 2019/8/13
version: 3.7.3
"""

##程式宣告區
fruit_name = []
fruit_price = []
fruit_num = []
fruit_total = []

##程式開始執行點
###輸入點
kinds = int(input("請輸入水果有多少種類: "))
for i in range(0,kinds):
    fruit_name.append(input("請輸入水果名稱: "))
    fruit_price.append(float(input("請輸入單價: ")))
    fruit_num.append(int(input("請輸入購買斤數: ")))



    ###運算式
    fruit_total.append(fruit_price[i] * fruit_num[i])
    #[i]表示要讓list裡每個區塊的數值做計算，不然系統會以整個List計算而產生錯誤


###輸出結果
print("{0:5s} {1:5s} {2:5s} {3:5s}".format("水果","單價","數量","總價"))
for j in range(0,kinds): 
    print("%2s  %5.1f  %5.1f  %5.1f" % (fruit_name[j],fruit_price[j],fruit_num[j],fruit_total[j]))

