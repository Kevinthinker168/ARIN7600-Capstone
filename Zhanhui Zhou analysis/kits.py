import pymysql
import time
import yfinance as yf
from pandas_datareader import data
import datetime
import os
import pandas as pd
yf.pdr_override()
db_map = {"test": "stock_data_test", "formal": "stock_data"}





def update(stock_name, env="formal"):
    database = db_map[env]
    db = pymysql.connect(
        user = "root",
        passwd = "123456",
        database = database
    )
    cursor = db.cursor()
    cursor.execute("SELECT last_date, last_update from data_status where stock_name='%s'"%stock_name)
    log("Update process for %s start."%stock_name)
    dates = cursor.fetchall()
    
    if dates:
        date, last_update = dates[0]
        now = get_now_date()[0]
        if last_update != now:
            start = get_next_date(date)
            stock_data, last_date = fetch_stock_data(stock_name, start = start)
            if last_date:
                cursor.execute("UPDATE data_status SET last_date = '%s', last_update = '%s' WHERE stock_name = '%s'"%(date, last_date, stock_name))
                log("Data of %s is updating"%stock_name)
                for i in range(len(stock_data)):
                    one_data = stock_data.iloc[i]
                    cursor.execute("INSERT INTO %s(Date, Open, High, Low, Close, Adj_Close, Volume) VALUES ('%s', %f, %f, %f, %f, %f, %i)"%(stock_name, 
                                                                                str(one_data.name).split(" ")[0], 
                                                                                one_data["Open"], 
                                                                                one_data["High"],
                                                                                one_data["Low"],
                                                                                one_data["Close"],
                                                                                one_data["Adj Close"],
                                                                                one_data["Volume"]
                                                                                ))
                log("Data of %s is updated, %i datas added."%(stock_name, len(stock_data)))
                cursor.close()
                db.commit()
                db.close()
    else: # no such data
        stock_data, last_date = fetch_stock_data(stock_name)
        if last_date:
            cursor.execute("INSERT INTO data_status VALUES('%s', '%s', '%s')"%(stock_name, last_date, get_now_date()[0]))
            log("New data_status of %s added."%(stock_name))
            cursor.execute("CREATE TABLE IF NOT EXISTS %s (Date VARCHAR(10), Open FLOAT, High FLOAT, Low FLOAT, Close FLOAT, Adj_Close FLOAT, Volume INT)"%stock_name)
            log("New table of %s added."%(stock_name))
            log("New data of %s is updating"%stock_name)
            for i in range(len(stock_data)):
                one_data = stock_data.iloc[i]
                cursor.execute("INSERT INTO %s(Date, Open, High, Low, Close, Adj_Close, Volume) VALUES ('%s', %f, %f, %f, %f, %f, %i)"%(stock_name, 
                                                                            str(one_data.name).split(" ")[0], 
                                                                            one_data["Open"], 
                                                                            one_data["High"],
                                                                            one_data["Low"],
                                                                            one_data["Close"],
                                                                            one_data["Adj Close"],
                                                                            one_data["Volume"]
                                                                            ))
            log("New data of %s is updated, %i datas added."%(stock_name, len(stock_data)))
            cursor.close()
            db.commit()
            db.close()
    log("Update process for %s ends."%stock_name)

def get_now_date():
    timestamp = int(time.time())
    struct_time = time.gmtime(timestamp)
    date = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
    now_date, now_time = date.split(' ')
    return now_date, now_time

def get_next_date(now_time):
    now_year, now_mon, now_date = now_time.split("-")
    now_date = datetime.date(year = int(now_year), month = int(now_mon), day = int(now_date))
    next_date = now_date + datetime.timedelta(days=1)
    return next_date.strftime("%Y-%m-%d")

def get_previous_date(now_time, delta_year=2):
    [now_year, now_mon, now_day] = now_time.split("-")
    return "-".join([str(int(now_year) - delta_year), now_mon, now_day])

def fetch_stock_data(stock_name, start="default", end = "default"):
    if end == "default":
        now_date, now_time = get_now_date()
        end = now_date
    if start == "default":
        start = get_previous_date(end)
    stock_data = data.get_data_yahoo(tickers=stock_name,start=start,end=end,progress=False)
    if len(stock_data) == 0:
        return None, None
    return stock_data, str(stock_data.index.tolist()[-1]).split(' ')[0]

def log(log):
    if not os.path.exists("./logs"):
        os.mkdir("./logs")
    struct_time = time.gmtime(time.time())
    date = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
    with open("./logs/log", "a") as f:
        f.write(date+": "+log+"\r\n")

def read_db(stock_name, date, env):
    update(stock_name, env)
    now_date = get_now_date()[0]
    if date > now_date:
        return None
    else:
        previous = get_previous_date(now_date)
        database = db_map[env]
        db = pymysql.connect(
            user = "root",
            passwd = "123456",
            database = database
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM %s WHERE Date < '%s' and Date >= '%s'"%(stock_name, date, previous))
        d = cursor.fetchall()
        df = pd.core.frame.DataFrame(d)
        df.columns = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
        df.set_index("Date", inplace=True)
        return df