import pandas as pd
import tushare as ts

from ..db import engine, TABLE_STOCK_BASICS_DAILY

'''
公司每日基本信息
相关接口 get_stock_basics

__tablename__ = 'Stock_basic'
id = Column(Integer, primary_key=True, autoincrement=True)
# 代码
code = Column(Integer, index=True)
# 股票名
name = Column(String)
# 日期 eg: 2017-11-24
date = Column(String)
# 市盈率 eg: 1033.02
pe = Column(Float)
# 流通股本 eg: 22.46
outstanding = Column(Float)
# 总股本(万) eg: 30.11
totals = Column(Float)
# 总资产(万) eg: 738695.50
totalAssets = Column(Float)
# 流动资产 eg: 375573.72
liquidAssets = Column(Float)
# 固定资产 eg: 108218.02
fixedAssets = Column(Float)
# 公积金 eg: 61736.45
reserved = Column(Float)
# 每股净资 eg: 2.11
bvps = Column(Float)
# 市净率 eg: 2.18
pb = Column(Float)
# 未分利润 eg: 259275.80
undp = Column(Float)
# 每股未分配 eg: 0.86
perundp = Column(Float)
# 收入同比( %) eg: -11.93
rev = Column(Float)
# 利润同比( %) eg: -5.31
profit = Column(Float)
# 毛利率( %) eg: 71.65
gpr = Column(Float)
# 净利润率(%) eg: 18.88
npr = Column(Float)
# 股东人数 eg: 71907.0
holders = Column(Float)
'''


def check_is_exist(date):
    '''
    检查指定日期数据是否已经存在
    :return:
    '''
    try:
        old_df = pd.read_sql("select * from '%s' where date = '%s'" % (TABLE_STOCK_BASICS_DAILY, date), engine)
        return old_df.size > 0
    except:
        return False


def fetch_stock_basics_daily(date_str):
    '''
    获取全部股票每日基本信息
    :param date_str:
    :return:
    '''
    df = ts.get_stock_basics(date_str)
    df['date'] = date_str
    return df

# sql_for_stock_basics('2010-11-20', '2017-11-27')
