import tushare as ts
from get_data import engine, TABLE_STOCK_BASICS
from utils.strutils import getEveryDay, date2str
import pandas as pd

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
        old_df = pd.read_sql("select * from '%s' where date = '%s'" % (TABLE_STOCK_BASICS, date), engine)
        return old_df.size > 0
    except:
        return False


def sql_for_stock_basics_date(date_str):
    '''
    将目标日期的 get_stock_basics 数据入库
    :param date_str:
    :return:
    '''

    if check_is_exist(date_str):
        print("该日期 %s 记录已存在" % date_str)
        return

    try:
        df = ts.get_stock_basics(date_str)
        df['date'] = date_str
        df.to_sql(TABLE_STOCK_BASICS, engine, if_exists='append')
    except:
        print("该日期 %s 没有数据" % date_str)


def sql_for_stock_basics(begin_date='1991-01-01', end_date=date2str()):
    '''
    将begin_date到end_date 的日期的数据全部入库 （注意数据不去重）
    数据可是是YYYY-MM-DD
    :param begin_date:
    :param end_date:
    :return:
    '''
    dates = getEveryDay(begin_date, end_date)[::-1]
    for date in dates:
        sql_for_stock_basics_date(date)

# sql_for_stock_basics('2010-11-20', '2017-11-27')
