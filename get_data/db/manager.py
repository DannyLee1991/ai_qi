import pandas as pd
from get_data.db import *


def write2db(df,table,if_exists):
    '''
    写入db
    :param df:
    :return:
    '''
    df.to_sql(table, engine, if_exists=if_exists)
    print("新数据插入成功 [table: %s ]" % (table))

# ---------------------------------------------------


def check_is_exist_in_stock_basics_daily(date):
    '''
    检查指定日期数据是否已经存在于股票基本信息中
    :return:
    '''
    try:
        old_df = pd.read_sql("select * from '%s' where date = '%s'" % (TABLE_STOCK_BASICS_DAILY, date), engine)
        return old_df.size > 0
    except:
        return False

def check_is_exist_in_tick(code, date):
    '''
    指定日期的股票记录是否存在
    :param code:
    :param date:
    :return:
    '''
    try:
        sql = "select date from %s where code = '%s' and date = '%s'" % (TABLE_TICK, code, date)
        df = pd.read_sql(sql, engine)
        return len(df) > 0
    except:
        return False