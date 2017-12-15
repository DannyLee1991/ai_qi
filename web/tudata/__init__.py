from .db import *
from .fetcher import *

from utils.strutils import getEveryDay, todayStr, perYearStr


def clear_data(table_name):
    '''
    清空某个表的数据
    :param table_name:
    :return:
    '''
    df = pd.DataFrame()
    df.to_sql(table_name, engine, if_exists='replace')


# --------------------------------------------------------

def fs_stock():
    '''
    获取股票数据 并入库
    :return:
    '''
    df = fetch_stock_basic()
    write2db(df, TN_STOCK, 'replace')


def fs_stock_industry():
    '''
    获取股票行业数据 并入库
    :return:
    '''
    df = fetch_stock_industry()
    write2db(df, TN_STOCK_INDUSTRY, 'replace')


def fs_stock_area():
    '''
    获取股票地区数据 并入库
    :return:
    '''
    df = fetch_stock_area()
    write2db(df, TN_STOCK_AREA, if_exists='replace')


def fs_stock_concept():
    '''
    获取股票概念数据 并入库
    :return:
    '''
    df = fetch_stock_concept()
    write2db(df, TN_STOCK_CONCEPT, if_exists='replace')


def fs_stock_basics_daily(date=todayStr(), del_duplicate=True):
    '''
    获取大盘某日股票基本信息数据 并入库
    :param date:
    :return:
    '''
    is_exist = check_is_exist_in_stock_basics_daily(date)
    if is_exist:
        print("该日期 %s 记录已存在" % date)
    else:
        try:
            df = fetch_stock_basics_daily(date)
            write2db(df, TN_STOCK_BASICS_DAILY, if_exists='append')

            if del_duplicate:
                _delete_duplicate_data(TN_STOCK_BASICS_DAILY, 'code', 'date')
        except:
            print("该日期 %s 没有数据" % date)


def fs_stock_basics_daily_r(begin_date, end_date, del_duplicate=True):
    '''
    获取大盘某个时间区间股票基本信息数据 并入库
    :param begin_date: YYYY-MM-DD
    :param end_date: YYYY-MM-DD
    :return:
    '''
    for date in getEveryDay(begin_date, end_date)[::-1]:
        fs_stock_basics_daily(date, del_duplicate=False)

    if del_duplicate:
        _delete_duplicate_data(TN_STOCK_BASICS_DAILY, 'code', 'date')


def fs_tick(code, date, del_duplicate=True):
    '''
    获取某只股票某天的分笔数据 并入库
    :param code:
    :param date:
    :return:
    '''
    if check_is_exist_in_tick(code, date):
        print("数据已存在 [code %s  date %s]" % (code, date))
    else:
        df = fetch_tick(code, date)
        if df is not None:
            write2db(df, TN_TICK, if_exists='append')
            if del_duplicate:
                _delete_duplicate_data(TN_TICK, 'code', 'date', 'time')


def fs_tick_r(code, begin_date, end_date, del_duplicate=True):
    '''
    获取某只股票具体时间区间的分笔数据 并入库
    :param code:
    :param begin_date:
    :param end_date:
    :return:
    '''
    for date in getEveryDay(begin_date, end_date)[::-1]:
        fs_tick(code, date, del_duplicate=False)

    if del_duplicate:
        _delete_duplicate_data(TN_TICK, 'code', 'date', 'time')


# @cache()
def fs_transaction_d(code, del_duplicate=True):
    '''
    获取某只股票的最新的日交易数据 并入库
    :param code:
    :return:
    '''
    ktype = 'D'
    s = start_date(code, ktype)
    if s is todayStr():
        print("%s 数据已是最新 无需获取 [%s]" % (str(code), s))
    else:
        df = fetch_transaction(code, s, ktype)
        write2db(df, TN_TRANSACTION_D, if_exists='append')

        if del_duplicate:
            _delete_duplicate_data(TN_TRANSACTION_D, 'code', 'date')


def fs_transaction_5min(code, del_duplicate=True):
    '''
    获取某只股票的最新的5分钟交易数据 并入库
    :param code:
    :return:
    '''
    ktype = '5'
    s = start_date(code, ktype)
    df = fetch_transaction(code, s, ktype)
    write2db(df, TN_TRANSACTION_5MIN, if_exists='append')

    if del_duplicate:
        _delete_duplicate_data(TN_TRANSACTION_5MIN, 'code', 'date')


def fs_transaction_d_all(del_duplicate=True):
    '''
    获取全部股票的最新的日交易数据 并入库
    :return:
    '''
    codes = all_codes()
    for index, code in enumerate(codes):
        print("当前进度 [%s/%s]" % (index, len(codes)))
        fs_transaction_d(code, del_duplicate=False)

    if del_duplicate:
        _delete_duplicate_data(TN_TRANSACTION_5MIN, 'code', 'date')


def fs_transaction_5min_all(del_duplicate=True):
    '''
    获取全部股票的最新的5分钟交易数据 并入库
    :return:
    '''
    codes = all_codes()
    for index, code in enumerate(codes):
        print("当前进度 [%s/%s]" % (index, len(codes)))
        fs_transaction_5min(code, del_duplicate=False)

    if del_duplicate:
        _delete_duplicate_data(TN_TRANSACTION_5MIN, 'code', 'date')


def fs_fuquan(code, start_date=perYearStr(), end_date=todayStr(), autype='qfq', del_duplicate=True):
    '''
    获取某个股票的复权数据 并入库
    :param code:
    :param start_date:
    :param end_date:
    :param autype:
    :return:
    '''
    if autype == 'none':
        autype = None

    s_date, e_date = gen_time_interval(code, autype, start_date, end_date)
    if s_date and e_date:
        df = fetch_fuquan(code, s_date, e_date, autype)
        write2db(df, TN_FUQUAN, 'append')

        if del_duplicate:
            _delete_duplicate_data(TN_FUQUAN, 'date', 'code', 'autype')
    else:
        print("%s数据已是最新，不需要重新获取")


def fs_fuquan_all(start_date=perYearStr(), end_date=todayStr(), autype='qfq', del_duplicate=True):
    '''
    获取全部股票的复权数据 并入库
    :param start_date:
    :param end_date:
    :param autype:
    :return:
    '''
    codes = all_codes()
    for code in codes:
        fs_fuquan(code, start_date, end_date, autype, del_duplicate=False)

    if del_duplicate:
        _delete_duplicate_data(TN_FUQUAN, 'date', 'code', 'autype')


def _delete_duplicate_data(table_name, *fields):
    '''
    删除重复数据
    :param table_name:
    :param fields:
    :return:
    '''
    execute_sql(sql_delete_duplicate_data(table_name, *fields))
