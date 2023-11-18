from flask import Flask, render_template, request
import pymysql
from kits import *
import json

database = "stock_data_test"
app = Flask(__name__)
db = pymysql.connect(
        user = "root",
        passwd = "123456",
        database = database
    )

app = Flask(__name__)
@app.route('/test')
def test():
    return "<h>服务器连接成功</h>"

@app.route("/predict", methods = ["GET"])
def predict():
    args = dict(request.args)
    if "stock_name" in args.keys():
        stock_name = args["stock_name"]
        stock_data = read_db(stock_name, date = get_now_date()[0], env = "test")
        return str(stock_data)
    else:
        return "Invalid stock name"
    

# @app.route('/update', methods = ["get"])
# def insert():
#     try:
#         form = request.form
#         test1 = form['test1']
#         test2 = form['test2']
#         test3 = form['test3']
#         mdb = u'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+mdb_path
#         conn = pyodbc.connect(mdb)
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO test_table VALUES('%s','%s','%s')"%(test1, test2, test3))
#         cursor.commit()
#         cursor.close()
#         conn.close()
#         return "<h>OK</h>"
#     except:
#         return "<h>ERROR</h>"
    
# @app.route("homepage")
# def homepage():
#     return "Hello"
# @app.route('/predict', methods = ["get"])
# def predict():
#     args = request.args
#     args_dict = args.to_dict()
#     stockname = args_dict["stockname"]
#     date = args_dict["date"]
    

#     queryKeys = list(args_dict.keys())
#     queryValues = list(args_dict.values())
#     queryConditon = ""
#     for i in range(len(queryKeys)):
#         queryConditon += queryKeys[i]+"='"+queryValues[i]+"' and "
#     queryConditon = queryConditon[:-5]
            

#     mdb = u'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+mdb_path
#     conn = pyodbc.connect(mdb)
#     cursor = conn.cursor()
#     data = None
#     if len(queryConditon) > 0:
#         data = cursor.execute("SELECT * FROM test_table WHERE "+queryConditon).fetchall()
#     cursor.commit()
#     cursor.close()
#     conn.close()
#     return "<h>%s</h>"%str(data)
    




if __name__ == "__main__":
    app.run()