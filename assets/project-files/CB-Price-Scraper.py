#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:56:26 2021

@author: matthewreisdorf
"""

from coinbase.wallet.client import Client
import json
import datetime
import sched, time

API_KEY = 'key'
API_SECRET = 'secret'

client = Client(API_KEY, API_SECRET)
ETH_Time_Price_List = []



BTC_USD = 'BTC-USD'
ETH_USD = 'ETH-USD'
LTC_USD = 'LTC-USD'

#ETH_price = client.get_spot_price(currency_pair = ETH_USD)
#BTC_price = client.get_spot_price(currency_pair = BTC_USD)
LTC_price = client.get_spot_price(currency_pair = LTC_USD)
client_time = client.get_time()


#ETH_Time_Price_List.append((ETH_price['amount'],client_time['iso']))



#print(ETH_Time_Price_List)




endTime = datetime.datetime.now() + datetime.timedelta(minutes = 1)


def priceAppend():
    
    EthList = []
    #BtcList = []
    
    while datetime.datetime.now() < endTime:
        
        ETH_price = client.get_spot_price(currency_pair = ETH_USD)
        #BTC_price = client.get_spot_price(currency_pair = BTC_USD)
        
        EthList.append((ETH_price['amount'],client_time['iso']))
        #BtcList.append(BTC_price['amount'])
        
        time.sleep(30)
        
        with open('/Users/matthewreisdorf/Desktop/Personal-Code/CB-Price-Scraper/CB-prices.json', 'a') as fp:
            json.dump(ETH_price, fp)
        
        
        
        
    return EthList


print(priceAppend())











#with open('/Users/matthewreisdorf/Desktop/Personal Code/CB Price Scraper/CB-prices.json', 'a') as fp:
    #json.dump(ETH_price, fp)
    #json.dump(time['iso'], fp)
    #json.dump(BTC_price, fp)
    #json.dump(LTC_price, fp)









#print(time)
#print(ETH_price)
#print(BTC_price)
#print(LTC_price)
