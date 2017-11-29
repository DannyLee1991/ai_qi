import tushare as ts
from get_data import engine
from get_data import distinct_codes, TABLE_TRANSACTION, TABLE_TRANSACTION_5MIN
from utils.strutils import nextDayStr, nextMinStr
from utils.strutils import date2str
import pandas as pd

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

def sql_for_transaction(ktype="D"):
    '''
    股票历史日K 交易数据 get_hist_data
    :return:
    '''
    codes = distinct_codes()
    size = len(codes)
    for index, code in enumerate(codes):
        print("当前进度 [%s/%s]" % (index, size))
        start_date = None

        try:
            # 获取最新数据的日期
            start_date = get_newest_date(code, start_date, ktype)
            if ktype is '5':
                start_date = nextMinStr(start_date)
            else:
                start_date = nextDayStr(start_date)
                if date2str() is start_date:
                    print("%s 数据已是最新 -- %s" % (str(code), start_date))
                    continue
        except:
            print("数据不存在，获取%s的全部历史记录" % (code))

        save_2_db(code, start_date, ktype)


def save_2_db(code, start_date, ktype='D'):
    '''
    获取数据并入库
    :param code:
    :param start_date:
    :param ktype:
    :return:
    '''
    df = ts.get_hist_data(code, start_date, ktype=ktype)
    df['code'] = code
    table = TABLE_TRANSACTION_5MIN if ktype is '5' else TABLE_TRANSACTION
    df.to_sql(table, engine, if_exists='append')


def get_newest_date(code, start_date, ktype='D'):
    '''
    获取最新的记录日期
    :param code:
    :param start_date:
    :param ktype:
    :return:
    '''
    if ktype is '5':
        table = TABLE_TRANSACTION_5MIN
    else:
        table = TABLE_TRANSACTION

    old_df = pd.read_sql("select date from '%s' where code = '%s'" % (table, str(code)), engine)

    # 当前记录中 当前股票的最新记录日期
    start_date = old_df['date'][0]
    return start_date


def sql_for_transaction_d():
    '''
    交易记录 - 每日
    :return:
    '''
    sql_for_transaction('D')

def sql_for_transaction_5min():
    '''
    交易记录 - 每5分钟
    :return:
    '''
    sql_for_transaction('5')

