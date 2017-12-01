import pandas as pd
import tushare as ts

from get_data.db import engine, TABLE_TRANSACTION_D, TABLE_TRANSACTION_5MIN
from utils.strutils import nextDayStr, nextMinStr

'''
个股历史交易记录
相关接口： get_hist_data

__tablename__ = 'transaction'
id = Column(Integer, primary_key=True, autoincrement=True)
# 代码
code = Column(Integer, index=True)
# 日期 eg: 2017-11-24
date = Column(String, index=True)
# 开盘价 eg: 24.10
open = Column(Float)
# 最高价 eg: 24.70
high = Column(Float)
# 收盘价 eg: 24.45
close = Column(Float)
# 最低价 eg: 24.09
low = Column(Float)
# 成交量 eg: 53160.52
volume = Column(Float)
# 价格变动 eg: 0.43
price_change = Column(Float)
# 涨跌幅 eg: 1.79
p_change = Column(Float)
# 5日均价 eg: 24.822
ma5 = Column(Float)
# 10日均价 eg: 26.441
ma10 = Column(Float)
# 20日均价 eg: 28.300
ma20 = Column(Float)
# 5日均量 eg: 80676.85
v_ma5 = Column(Float)
# 10日均量 eg: 117984.89
v_ma10 = Column(Float)
# 20日均量 eg: 175389.32
v_ma20 = Column(Float)
# 换手率 eg: 1.33
turnover = Column(Float) 
'''


def start_date(code, ktype):
    try:
        newest_date = get_newest_date(code, ktype)
        if ktype is '5':
            r = nextMinStr(newest_date)
        else:
            r = nextDayStr(newest_date)
        return r
    except:
        return None


def fetch_transaction(code, date, ktype):
    '''
    获取交易数据
    :param code:
    :param date:
    :param ktype:
    :return:
    '''
    df = ts.get_hist_data(code, start=date, ktype=ktype)
    df['code'] = code
    return df


def get_newest_date(code, ktype='D'):
    '''
    获取最新的记录日期
    :param code:
    :param ktype:
    :return:
    '''
    if ktype is '5':
        table = TABLE_TRANSACTION_5MIN
    else:
        table = TABLE_TRANSACTION_D

    df = pd.read_sql("select date from '%s' where code = '%s'" % (table, str(code)), engine)

    # 当前记录中 当前股票的最新记录日期
    return df['date'][0]
