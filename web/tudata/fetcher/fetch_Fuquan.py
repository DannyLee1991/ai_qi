import pandas as pd
import tushare as ts
from utils.pdutils import difference
from utils.strutils import nextDayStr, perDayStr

from ..db import TN_FUQUAN, read_sql

'''
复权数据
相关接口： get_h_data
__tablename__ = 'fuquan'
id = Column(Integer, primary_key=True, autoincrement=True)
# 代码
code = Column(Integer, index=True)
# 复权类型 eg: qfq
autype = Column(String)
# 交易日期 eg: 2017-11-24
date = Column(String, index=True)
# 开盘价 eg: 13.11
open = Column(Float)
# 最高价 eg: 13.18
high = Column(Float)
# 收盘价 eg: 13.09
close = Column(Float)
# 最低价 eg: 12.93
low = Column(Float)
# 成交量 eg: 59612483.0
volume = Column(Float)
# 成交金额 eg: 7.776997e+08
amount = Column(BIGINT)
'''


def get_diff_set(q_df, n_df):
    '''
    获取数据差集
    :param q_df: 查询结果
    :param n_df: 获取的线上数据
    :return:
    '''
    d_df = n_df
    if q_df is not None:
        d_df = difference(n_df, q_df, on=['code', 'autype'])
    return d_df


def fetch_fuquan(code, start, end, autype):
    '''
    获取数据
    :param code:
    :param start:
    :param end:
    :param autype:
    :return:
    '''
    n_df = ts.get_h_data(code=code, start=start, end=end, autype=autype)
    n_df['code'] = code
    n_df['autype'] = autype
    return n_df


def query_date(code, autype, type='newest'):
    '''
    查询历史记录
    :param code:
    :param autype:
    :param type: 'newest' 最新记录日期， 'oldest' 最老记录日期
    :return: YYYY-MM-DD
    '''
    result = None
    try:
        way = 'asc'
        if type is 'oldest':
            way = 'desc'

        sql = "select date from %s where code = '%s' and autype = '%s' order by date %s limit 1" % (
            TN_FUQUAN, code, autype, way)

        df = read_sql(sql)
        result = df.date[0][:10]
    except:
        print("历史数据不存在")
    finally:
        return result


def gen_time_interval(code, autype, start_date, end_date):
    '''
    获取可用的时间区间
    如果返回为空，则代表不存在可用的时间区间
    :param code:
    :param autype:
    :param start_date:
    :param end_date:
    :return:
    '''
    # 最新日期
    newest_date = query_date(code=code, autype=autype, type='newest')
    # 最老日期
    oldest_date = query_date(code=code, autype=autype, type='oldest')

    if newest_date and oldest_date:
        if end_date > newest_date:
            s_date = nextDayStr(oldest_date)
            e_date = end_date
        else:
            s_date = start_date
            e_date = perDayStr(oldest_date)

        if s_date > e_date:
            return s_date, e_date
        return None, None
    else:
        # 历史数据不存在，不需要处理 直接返回
        return start_date, end_date
