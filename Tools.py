import pandas as pd
import yfinance as yf
from pandas_datareader import data
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import talib 
from dateutil.relativedelta import relativedelta

yf.pdr_override()

def pct_change(stockname,start,end):
    stockdata=data.get_data_yahoo(tickers=stockname,start=start,end=end,progress=False)
    stockdata['Close_price_percentage'] = stockdata['Close'].pct_change()
    stockdata['real_situation'] = 0
    stockdata.loc[stockdata['Close_price_percentage'] > 0,'real_situation'] = "涨"
    stockdata.loc[stockdata['Close_price_percentage'] < 0,'real_situation'] ='跌'
    stockdata.loc[stockdata['Close_price_percentage'] == 0,'real_situation'] ='不变'
    return stockdata



def MACD(data):
    data['EMA12'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=26, adjust=False).mean()
    data['DIF'] = data['EMA12'] - data['EMA26']
    data['MACD'] = data['DIF'].ewm(span=9, adjust=False).mean()
    data['Position'] = 0
    data.loc[data['DIF'] > data['MACD'],'Position'] = 1
    data.loc[data['DIF'] < data['MACD'],'Position'] = -1
    return data

def MACD_short(data):
    data['EMA6'] = data['Close'].ewm(span=6, adjust=False).mean()
    data['EMA19'] = data['Close'].ewm(span=19, adjust=False).mean()
    data['DIF'] = data['EMA6'] - data['EMA19']
    data['MACD'] = data['DIF'].ewm(span=9, adjust=False).mean()
    data['Position'] = 0
    data.loc[data['DIF'] > data['MACD'],'Position'] = 1
    data.loc[data['DIF'] < data['MACD'],'Position'] = -1
    return data

def MACD_long(data):
    data['EMA19'] = data['Close'].ewm(span=19, adjust=False).mean()
    data['EMA39'] = data['Close'].ewm(span=39, adjust=False).mean()
    data['DIF'] = data['EMA19'] - data['EMA39']
    data['MACD'] = data['DIF'].ewm(span=9, adjust=False).mean()
    data['Position'] = 0
    data.loc[data['DIF'] > data['MACD'],'Position'] = 1
    data.loc[data['DIF'] < data['MACD'],'Position'] = -1
    return data


def RSI(data):
    # 短期
    rsi_6 = talib.RSI(data["Close"],timeperiod=6)
    data["RSI6"]=rsi_6
    # 中期
    rsi_14 = talib.RSI(data["Close"],timeperiod=14)
    data["RSI14"]=rsi_14
    #长期
    rsi_21 = talib.RSI(data["Close"],timeperiod=21)
    data["RSI21"]=rsi_21
    return data
def RSI_MACD(data,rsi,upper,lower):
    if rsi==6:
        data.loc[data['RSI6'] > upper,'Position'] = -1
        data.loc[data['RSI6'] < lower,'Position'] = 1
    elif rsi==14:
        data.loc[data['RSI14'] > upper,'Position'] = -1
        data.loc[data['RSI14'] < lower,'Position'] = 1
    elif rsi==21:
        data.loc[data['RSI21'] > upper,'Position'] = -1
        data.loc[data['RSI21'] < lower,'Position'] = 1
    return data
        

def results(data):
    close_price=list(data["Close"])
    signal=list(data["Position"])
    real_situation=list(data["real_situation"])
    total_day=len(real_situation)
    # 一直持有收益
    #假设持有1000股
    first_day =close_price[0]
    last_day =close_price[-1]
    value_diff=(last_day-first_day)*1000
    
    #prediction_rate
    i=0
    count=0
    while i<len(real_situation):
        if real_situation[i]=="涨" and signal[i]==1:
            count+=1
        elif real_situation[i]=="跌" and signal[i]==-1:
            count+=1
        i+=1
    rate=count/total_day
   
    #策略收益
    i=1
    revenue=0
    buy_price=close_price[0]
    
    while i<len(close_price)-1:
        if signal[i]==0:
            i+=1
        
        elif signal[i]==1 and signal[i+1]==1:
            
            i+=1
        elif signal[i]==1 and signal[i+1]==-1:
            profit=close_price[i+1]-buy_price
            revenue+= profit
            
            i+=1
        elif signal[i]==-1 and signal[i+1]==-1:
            
            i+=1
        elif signal[i]==-1 and signal[i+1]==1:
            buy_price=close_price[i+1]
            
            i+=1
    strategy=revenue*1000
   
    return rate,value_diff,strategy


#days collector
def days(months):
    day_collector=[]
    i=1
    while i<months:
        #current_date = datetime.now()
        current_date = datetime(year=2023, month=9, day=20)
        previous_date = current_date - relativedelta(months=i)
        previous_date  = previous_date.strftime("%Y-%m-%d")
        day_collector.append(previous_date)
        i+=1
    return day_collector
