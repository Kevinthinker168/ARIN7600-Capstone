import pandas as pd
import yfinance as yf
from pandas_datareader import data
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import talib 
import numpy as np
from dateutil.relativedelta import relativedelta

yf.pdr_override()

#Liangfan Xiao work
def days(months):
    day_collector=[]
    i=1
    while i<months:
        #current_date = datetime.now()
        current_date = datetime(year=2022, month=12, day=31)
        previous_date = current_date - relativedelta(months=i)
        previous_date  = previous_date.strftime("%Y-%m-%d")
        day_collector.append(previous_date)
        i+=1
    return day_collector

def pct_change(stockname,start,end):
    stockdata=data.get_data_yahoo(tickers=stockname,start=start,end=end,progress=False)
    stockdata['Close_price_percentage'] = stockdata['Close'].pct_change()
    stockdata['real_situation'] = 0
    stockdata.loc[stockdata['Close_price_percentage'] > 0,'real_situation'] = "涨"
    stockdata.loc[stockdata['Close_price_percentage'] < 0,'real_situation'] ='跌'
    stockdata.loc[stockdata['Close_price_percentage'] == 0,'real_situation'] ='不变'
    stockdata["log_return"] = np.log(stockdata['Close'])-np.log(stockdata['Close'].shift(1))
    
    #Zhanhui Zhou create features
    open_price = stockdata["Open"]
    stockdata["re_close"] = (stockdata["Close"] - stockdata["Low"])/(stockdata["High"] - stockdata["Low"])
    stockdata["re_open"] = (stockdata["Open"] - stockdata["Low"])/(stockdata["High"] - stockdata["Low"])
    
    
    stockdata = stockdata.dropna()
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




#Zhanhui Zhou work
def my_rsi(stock_datas, span):
    stock_data = stock_datas.copy()
    open_price = stock_data.loc[:,"Open"]
    close_price = stock_data.loc[:,"Close"]
    up_or_down = close_price - open_price
    abs_up_or_down = abs(close_price - open_price)
    window_start = 0
    window_end = 0
    now_abs_sum = 0
    now_raise_sum = 0
    res = []
    for window_end in range(len(up_or_down)):
        now_abs_sum += abs_up_or_down[window_end]
        now_raise_sum += max(up_or_down[window_end], 0)
        if window_end > span:
            now_abs_sum -= abs_up_or_down[window_start]
            now_raise_sum -= max(up_or_down[window_start], 0)
            window_start += 1
        res.append(now_raise_sum/now_abs_sum)
    stock_data["my_rsi"] = res
    return stock_data

class account:
    def __init__(self, stock_data):
        self.stock_data = stock_data.copy()
        self.isHold = 0
        self.signal = list(self.stock_data["Position"])
        self.log_return = list(self.stock_data["log_return"])
        self.real_situation = list(self.stock_data["real_situation"])
        self.rate = -1
        self.buy_and_hold = None
        self.strategy = None

    def _cal_rate(self):
        precise = 0
        for i in range(len(self.real_situation)):
            if self.real_situation[i]=="涨" and self.signal[i]==1:
                precise += 1
            elif self.real_situation[i]=="跌" and self.signal[i]==-1:
                precise += 1
        self.rate = precise / len(self.real_situation)

    def _cal_buy_and_hold(self):
        self.buy_and_hold = sum(self.log_return)

    def _strategy(self, trade_day):
        if self.signal[trade_day]==0 and self.signal[trade_day+1]==0:
            return 0
            
        elif self.signal[trade_day]==0 and self.signal[trade_day+1]==1:
            return 1
            
        elif self.signal[trade_day]==0 and self.signal[trade_day+1]==-1:
            return 0
            
        elif self.signal[trade_day]==1 and self.signal[trade_day+1]==1:
            return 0
            
        elif self.signal[trade_day]==1 and self.signal[trade_day+1]==-1:
            return 1
            
        elif self.signal[trade_day]==1 and self.signal[trade_day+1]==0:
            return 0
            
        elif self.signal[trade_day]==-1 and self.signal[trade_day+1]==-1:
            return 0
            
        elif self.signal[trade_day]==-1 and self.signal[trade_day+1]==1:
            return 1
            
        elif self.signal[trade_day]==-1 and self.signal[trade_day+1]==0:
            return 0

    def _cal_strategy(self):
        log_return = 0
        for trade_day in range(len(self.log_return) - 1):
            if self._strategy(trade_day):
                if self.isHold:
                    log_return += self.log_return[trade_day]
                self.isHold = 1 - self.isHold
            else:
                if self.isHold:
                    log_return += self.log_return[trade_day]
        self.strategy = log_return

    def result(self):
        self._cal_rate()
        self._cal_buy_and_hold()
        self._cal_strategy()
        return [self.rate, self.buy_and_hold, self.strategy]
    
def preprocessor(stock_data, funcs_params):
    for func_param in funcs_params:
        if func_param[1]:
            stock_data = func_param[0](stock_data, func_param[1][0],
                                       func_param[1][1],
                                       func_param[1][2],)
        else:
            stock_data = func_param[0](stock_data)
    return stock_data

def test_fun(stock_datas, funcs_params):
    rate=[]
    holding = []
    strategy=[]
    for data in stock_datas:
        stock_data = data.copy()
        stock_data=preprocessor(stock_data, funcs_params)
        acc = account(stock_data)
        result = acc.result()
        rate.append(result[0])
        holding.append(result[1])
        strategy.append(result[2])
    return rate, holding, strategy
