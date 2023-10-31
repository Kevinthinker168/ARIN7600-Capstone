import pandas as pd
import yfinance as yf
from pandas_datareader import data
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import talib 
from dateutil.relativedelta import relativedelta

from Tool_v1 import *

yf.pdr_override()

#根据指标找出在两年回测时间段中收益最好的策略

def Best_result(name,start,end):
    name=name
    start=start
    end=end
    
    
    information=[]
    
    stock_datas=[pct_change(name,start,end)]
 
    
#MACD_12_26
    
#     stock_data=pct_change(name,start,end)
#     stock_data=MACD(stock_data)
    
#     result=results(stock_data)
#     result.append('MACD_12_26')
#     information.append(result)
    
    funcs_params = [(MACD, None)]
    rate1, holding, strategy1 = test_fun(stock_datas, funcs_params)
    rate1.append('MACD_12_26')
    strategy1.append('MACD_12_26')


#MACD_6_19


#     stock_data=pct_change(name,start,end)
#     stock_data=MACD_short(stock_data)
    
#     result=results(stock_data)
#     result.append('MACD_6_19')
#     information.append(result)
    
    funcs_params = [(MACD_short, None)]
    rate2, _, strategy2 = test_fun(stock_datas, funcs_params)
    rate2.append('MACD_6_19')
    strategy2.append('MACD_6_19')
    
#MACD_19_39

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD_long(stock_data)
#     result=results(stock_data)
#     result.append('MACD_19_39')
#     information.append(result)

    funcs_params = [(MACD_long, None)]
    rate3, _, strategy3 = test_fun(stock_datas, funcs_params)
    rate3.append('MACD_19_39')
    strategy3.append('MACD_19_39')


####################
#MACD619RSI6_8020
#     stock_data=pct_change(name,start,end)
#     stock_data=MACD_short(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,6,80,20)
    
#     result=results(stock_data)
#     result.append('MACD619RSI6_8020')
#     information.append(result)
    
    funcs_params = [
    (MACD_short, None), 
    (RSI, None), 
    (RSI_MACD, (6,80,20))]
    rate4, _, strategy4 = test_fun(stock_datas, funcs_params)
    rate4.append('MACD619RSI6_8020')
    strategy4.append('MACD619RSI6_8020')

#MACD619RSI6_7030

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD_short(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,6,70,30)
    
#     result=results(stock_data)
#     result.append('MACD619RSI6_7030')
#     information.append(result)
    
    funcs_params = [
    (MACD_short, None), 
    (RSI, None), 
    (RSI_MACD, (6,70,30))]
    rate5, _, strategy5 = test_fun(stock_datas, funcs_params)
    rate5.append('MACD619RSI6_7030')
    strategy5.append('MACD619RSI6_7030')
    
    
#MACD619RSI14_8020

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD_short(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,14,80,20)
    
#     result=results(stock_data)
#     result.append('MACD619RSI14_8020')
#     information.append(result)
    
    funcs_params = [
    (MACD_short, None), 
    (RSI, None), 
    (RSI_MACD, (14,80,20))]
    rate6, _, strategy6 = test_fun(stock_datas, funcs_params)
    rate6.append('MACD619RSI14_8020')
    strategy6.append('MACD619RSI14_8020')
    
#MACD619RSI14_7030

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD_short(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,14,70,30)
  
#     result=results(stock_data)
#     result.append('MACD619RSI14_7030')
#     information.append(result)
    
    funcs_params = [
    (MACD_short, None), 
    (RSI, None), 
    (RSI_MACD, (14,70,30))]
    rate7, _, strategy7 = test_fun(stock_datas, funcs_params)
    rate7.append('MACD619RSI14_7030')
    strategy7.append('MACD619RSI14_7030')
    
#MACD619RSI21_8020

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD_short(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,21,80,20)
    
#     result=results(stock_data)
#     result.append('MACD619RSI21_8020')
#     information.append(result)
    
    funcs_params = [
    (MACD_short, None), 
    (RSI, None), 
    (RSI_MACD, (21,80,20))]
    rate8, _, strategy8 = test_fun(stock_datas, funcs_params)
    rate8.append('MACD619RSI21_8020')
    strategy8.append('MACD619RSI21_8020')
    
#MACD619RSI21_7030

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD_short(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,21,70,30)
    
#     result=results(stock_data)
#     result.append('MACD619RSI21_7030')
#     information.append(result)
    
    funcs_params = [
    (MACD_short, None), 
    (RSI, None), 
    (RSI_MACD, (21,70,30))]
    rate9, _, strategy9 = test_fun(stock_datas, funcs_params)
    rate9.append('MACD619RSI21_7030')
    strategy9.append('MACD619RSI21_7030')
    


#######################
#MACD1939RSI6_8020

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD_long(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,6,80,20)
    
#     result=results(stock_data)
#     result.append('MACD1939RSI6_8020')
#     information.append(result)
    
    funcs_params = [
    (MACD_long, None), 
    (RSI, None), 
    (RSI_MACD, (6,80,20))]
    rate10, _, strategy10 = test_fun(stock_datas, funcs_params)
    rate10.append('MACD1939RSI6_8020')
    strategy10.append('MACD1939RSI6_8020')

#MACD1939RSI6_7030

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD_long(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,6,70,30)
    
#     result=results(stock_data)
#     result.append('MACD1939RSI6_7030')
#     information.append(result)
    
    funcs_params = [
    (MACD_long, None), 
    (RSI, None), 
    (RSI_MACD, (6,70,30))]
    rate11, _, strategy11 = test_fun(stock_datas, funcs_params)
    rate11.append('MACD1939RSI6_7030')
    strategy11.append('MACD1939RSI6_7030')
    
#MACD1939RSI14_8020

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD_long(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,14,80,20)
    
#     result=results(stock_data)
#     result.append('MACD1939RSI14_8020')
#     information.append(result)
    
    funcs_params = [
    (MACD_long, None), 
    (RSI, None), 
    (RSI_MACD, (14,80,20))]
    rate12, _, strategy12 = test_fun(stock_datas, funcs_params)
    rate12.append('MACD1939RSI14_8020')
    strategy12.append('MACD1939RSI14_8020')
    
#MACD1939RSI14_7030

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD_long(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,14,70,30)
    
#     result=results(stock_data)
#     result.append('MACD1939RSI14_7030')
#     information.append(result)
    
    funcs_params = [
    (MACD_long, None), 
    (RSI, None), 
    (RSI_MACD, (14,70,30))]
    rate13, _, strategy13 = test_fun(stock_datas, funcs_params)
    rate13.append('MACD1939RSI14_7030')
    strategy13.append('MACD1939RSI14_7030')
    
#MACD1939RSI21_8020
#     stock_data=pct_change(name,start,end)
#     stock_data=MACD_long(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,21,80,20)
    
#     result=results(stock_data)
#     result.append('MACD1939RSI21_8020')
#     information.append(result)
    
    funcs_params = [
    (MACD_long, None), 
    (RSI, None), 
    (RSI_MACD, (21,80,20))]
    rate14, _, strategy14 = test_fun(stock_datas, funcs_params)
    rate14.append('MACD1939RSI21_8020')
    strategy14.append('MACD1939RSI21_8020')
    
#MACD1939RSI21_7030

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD_long(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,21,70,30)
    
#     result=results(stock_data)
#     result.append('MACD1939RSI21_7030')
#     information.append(result)
    
    funcs_params = [
    (MACD_long, None), 
    (RSI, None), 
    (RSI_MACD, (21,70,30))]
    rate15, _, strategy15 = test_fun(stock_datas, funcs_params)
    rate15.append('MACD1939RSI21_7030')
    strategy15.append('MACD1939RSI21_7030')
    
########################################
#MACD1226RSI6_8020

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,6,80,20)
    
#     result=results(stock_data)
#     result.append('MACD1226RSI6_8020')
#     information.append(result)
    
    funcs_params = [
    (MACD, None), 
    (RSI, None), 
    (RSI_MACD, (6,80,20))]
    rate16, _, strategy16 = test_fun(stock_datas, funcs_params)
    rate16.append('MACD1226RSI6_8020')
    strategy16.append('MACD1226RSI6_8020')

#MACD1226RSI6_7030

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,6,70,30)
    
#     result=results(stock_data)
#     result.append('MACD1226RSI6_7030')
#     information.append(result)
    
    funcs_params = [
    (MACD, None), 
    (RSI, None), 
    (RSI_MACD, (6,70,30))]
    rate17, _, strategy17 = test_fun(stock_datas, funcs_params)
    rate17.append('MACD1226RSI6_7030')
    strategy17.append('MACD1226RSI6_7030')
    
    
#MACD1226RSI14_8020

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,14,80,20)
    
#     result=results(stock_data)
#     result.append('MACD1226RSI14_8020')
#     information.append(result)
    
    funcs_params = [
    (MACD, None), 
    (RSI, None), 
    (RSI_MACD, (14,80,20))]
    rate18, _, strategy18 = test_fun(stock_datas, funcs_params)
    rate18.append('MACD1226RSI14_8020')
    strategy18.append('MACD1226RSI14_8020')
    
#MACD1226RSI14_7030

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,14,70,30)
    
#     result=results(stock_data)
#     result.append('MACD1226RSI14_7030')
#     information.append(result)
    
    funcs_params = [
    (MACD, None), 
    (RSI, None), 
    (RSI_MACD, (14,70,30))]
    rate19, _, strategy19 = test_fun(stock_datas, funcs_params)
    rate19.append('MACD1226RSI14_7030')
    strategy19.append('MACD1226RSI14_7030')
    
#MACD1226RSI21_8020

#     stock_data=pct_change(name,start,end)
#     stock_data=MACD(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,21,80,20)
    
#     result=results(stock_data)
#     result.append('MACD1226RSI21_8020')
#     information.append(result)
    
    funcs_params = [
    (MACD, None), 
    (RSI, None), 
    (RSI_MACD, (21,80,20))]
    rate20, _, strategy20 = test_fun(stock_datas, funcs_params)
    rate20.append('MACD1226RSI21_8020')
    strategy20.append('MACD1226RSI21_8020')
    
#MACD1226RSI21_7030

#     stock_data=pct_change(name,start,end)    
#     stock_data=MACD(stock_data)
#     stock_data=RSI(stock_data)
#     stock_data=RSI_MACD(stock_data,21,70,30)
    
#     result=results(stock_data)
#     result.append('MACD1226RSI21_7030')
#     information.append(result)
    
    funcs_params = [
    (MACD, None), 
    (RSI, None), 
    (RSI_MACD, (21,70,30))]
    rate21, _, strategy21 = test_fun(stock_datas, funcs_params)
    rate21.append('MACD1226RSI21_7030')
    strategy21.append('MACD1226RSI21_7030')
    
    rate_col=[rate1,rate2,rate3,rate4,rate5,rate6,rate7,rate8,rate9,rate10,rate11,rate12,rate13,rate14,rate15,rate16,rate17,rate18,rate19,rate20,rate21]
    strategy_col=[strategy1,strategy2,strategy3,strategy4,strategy5,strategy6,strategy7,strategy8,strategy9,strategy10,strategy11,strategy12,strategy13,strategy14,strategy15,strategy16,strategy17,strategy18,strategy19,strategy20,strategy21]
    
    collection=[]
    count=0
    while count <len(rate_col):
        unit=[rate_col[count][0],strategy_col[count][0],strategy_col[count][1]]
        collection.append(unit)
        count+=1
    
    best_prediction_rate=collection[0]
    best_strategy=collection[0]
    
    
    i=0
    while i <len(collection):
        if collection[i][0]>=best_prediction_rate[0]:
            
        
            best_prediction_rate=collection[i]
            
        if collection[i][1]>=best_strategy[1]:
            
            best_strategy=collection[i]
            
       
        i+=1
    
    return best_prediction_rate, best_strategy,holding
            
            
        
    
    
    
    
 