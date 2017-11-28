from db import engine
import tushare as ts
import pandas as pd

def distinct_codes():
    '''
    获取不重复的股票代码
    :return:
    '''
    r = pd.read_sql("select code from stock", engine)
    codes = r['code']
    return codes