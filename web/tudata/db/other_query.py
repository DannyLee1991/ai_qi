from .base import *

def check_is_exist_in_stock_basics_daily(date):
    '''
    检查指定日期数据是否已经存在于股票基本信息中
    :return:
    '''
    df = read_sql("select * from '%s' where date = '%s'" % (TN_STOCK_BASICS_DAILY, date))
    if df is not None:
        return len(df) > 0
    else:
        return False


def check_is_exist_in_tick(code, date):
    '''
    指定日期的股票记录是否存在
    :param code:
    :param date:
    :return:
    '''
    df = read_sql("select date from %s where code = '%s' and date = '%s'" % (TN_TICK, code, date))
    if df is not None:
        return len(df) > 0
    else:
        return False