from .common_query import *
from .sql_builder import *
from . import *


# ---------------------------------------------------

def check_is_exist_in_stock_basics_daily(date):
    '''
    检查指定日期数据是否已经存在于股票基本信息中
    :return:
    '''
    try:
        old_df = pd.read_sql("select * from '%s' where date = '%s'" % (T_STOCK_BASICS_DAILY, date), engine)
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
        sql = "select date from %s where code = '%s' and date = '%s'" % (T_TICK, code, date)
        df = pd.read_sql(sql, engine)
        return len(df) > 0
    except:
        return False


