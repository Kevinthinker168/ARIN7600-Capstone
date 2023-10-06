import pandas as pd
import yfinance as yf
from pandas_datareader import data
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import talib 
from dateutil.relativedelta import relativedelta

from Tools import *
yf.pdr_override()


def Best_result(name,start,end):
    name=name
    start=start
    end=end
    
    
    information=[]
    
#MACD_12_26
    
    
    stock_data=pct_change(name,start,end)
    stock_data=MACD(stock_data)
    
    result=results(stock_data)
    result.append('MACD_12_26')
    information.append(result)

    
#MACD_6_19


    stock_data=pct_change(name,start,end)
    stock_data=MACD_short(stock_data)
    
    result=results(stock_data)
    result.append('MACD_6_19')
    information.append(result)
    
#MACD_19_39

    stock_data=pct_change(name,start,end)
    stock_data=MACD_long(stock_data)
    result=results(stock_data)
    result.append('MACD_19_39')
    information.append(result)

####################
#MACD619RSI6_8020
    stock_data=pct_change(name,start,end)
    stock_data=MACD_short(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,6,80,20)
    
    result=results(stock_data)
    result.append('MACD619RSI6_8020')
    information.append(result)

#MACD619RSI6_7030

    stock_data=pct_change(name,start,end)
    stock_data=MACD_short(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,6,70,30)
    
    result=results(stock_data)
    result.append('MACD619RSI6_7030')
    information.append(result)
    
    
#MACD619RSI14_8020

    stock_data=pct_change(name,start,end)
    stock_data=MACD_short(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,14,80,20)
    
    result=results(stock_data)
    result.append('MACD619RSI14_8020')
    information.append(result)
    
#MACD619RSI14_7030

    stock_data=pct_change(name,start,end)
    stock_data=MACD_short(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,14,70,30)
  
    result=results(stock_data)
    result.append('MACD619RSI14_7030')
    information.append(result)
    
#MACD619RSI21_8020

    stock_data=pct_change(name,start,end)
    stock_data=MACD_short(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,21,80,20)
    
    result=results(stock_data)
    result.append('MACD619RSI21_8020')
    information.append(result)
    
#MACD619RSI21_7030

    stock_data=pct_change(name,start,end)
    stock_data=MACD_short(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,21,70,30)
    
    result=results(stock_data)
    result.append('MACD619RSI21_7030')
    information.append(result)
    


#######################
#MACD1939RSI6_8020

    stock_data=pct_change(name,start,end)
    stock_data=MACD_long(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,6,80,20)
    
    result=results(stock_data)
    result.append('MACD1939RSI6_8020')
    information.append(result)

#MACD1939RSI6_7030

    stock_data=pct_change(name,start,end)
    stock_data=MACD_long(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,6,70,30)
    
    result=results(stock_data)
    result.append('MACD1939RSI6_7030')
    information.append(result)
    
    
#MACD1939RSI14_8020

    stock_data=pct_change(name,start,end)
    stock_data=MACD_long(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,14,80,20)
    
    result=results(stock_data)
    result.append('MACD1939RSI14_8020')
    information.append(result)
    
#MACD1939RSI14_7030

    stock_data=pct_change(name,start,end)
    stock_data=MACD_long(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,14,70,30)
    
    result=results(stock_data)
    result.append('MACD1939RSI14_7030')
    information.append(result)
    
#MACD1939RSI21_8020
    stock_data=pct_change(name,start,end)
    stock_data=MACD_long(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,21,80,20)
    
    result=results(stock_data)
    result.append('MACD1939RSI21_8020')
    information.append(result)
    
#MACD1939RSI21_7030

    stock_data=pct_change(name,start,end)
    stock_data=MACD_long(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,21,70,30)
    
    result=results(stock_data)
    result.append('MACD1939RSI21_7030')
    information.append(result)
########################################
#MACD1226RSI6_8020

    stock_data=pct_change(name,start,end)
    stock_data=MACD(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,6,80,20)
    
    result=results(stock_data)
    result.append('MACD1226RSI6_8020')
    information.append(result)

#MACD1226RSI6_7030

    stock_data=pct_change(name,start,end)
    stock_data=MACD(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,6,70,30)
    
    result=results(stock_data)
    result.append('MACD1226RSI6_7030')
    information.append(result)
    
    
#MACD1226RSI14_8020

    stock_data=pct_change(name,start,end)
    stock_data=MACD(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,14,80,20)
    
    result=results(stock_data)
    result.append('MACD1226RSI14_8020')
    information.append(result)
    
#MACD1226RSI14_7030

    stock_data=pct_change(name,start,end)
    stock_data=MACD(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,14,70,30)
    
    result=results(stock_data)
    result.append('MACD1226RSI14_7030')
    information.append(result)
    
#MACD1226RSI21_8020

    stock_data=pct_change(name,start,end)
    stock_data=MACD(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,21,80,20)
    
    result=results(stock_data)
    result.append('MACD1226RSI21_8020')
    information.append(result)
    
#MACD1226RSI21_7030

    stock_data=pct_change(name,start,end)    
    stock_data=MACD(stock_data)
    stock_data=RSI(stock_data)
    stock_data=RSI_MACD(stock_data,21,70,30)
    
    result=results(stock_data)
    result.append('MACD1226RSI21_7030')
    information.append(result)
    
    best_prediction_rate=information[0]
    best_strategy=information[0]
    
    i=0
    while i <len(information):
        if information[i][0]>=best_prediction_rate[0]:
            best_prediction_rate=information[i]
        if information[i][2]>=best_strategy[2]:
            best_strategy=information[i]
       
        i+=1
    
    return best_prediction_rate, best_strategy
            
            
        
    
    
    
    
 