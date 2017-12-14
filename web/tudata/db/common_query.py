from .base import *
from utils import strutils


@cache(use_mem=True)
def all_codes():
    '''
    获取不重复的股票代码
    :return:
    '''
    r = execute_sql("select distinct code from %s" % TN_STOCK)
    if r is not None:
        return r['code']
    else:
        print("stock表不存在，请先获取stock相关数据再执行此操作")

def all_trans_d_code():
    r = execute_sql("select distinct code from %s" % TN_TRANSACTION_D)
    if r is not None:
        return r['code']


def queryCode(queryWord):
    '''
    解析查询逻辑
    :param queryWord:
    :return:
    '''
    code = None
    if queryWord:
        if queryWord.isdigit():
            code = queryWord
        else:
            index = queryWord.find('(')
            if index != -1:
                name = queryWord[:index]
            else:
                name = queryWord
            code = query_code_by_name(name)
    return code


def query_code_by_name(name):
    '''
    根据股票名称查询id
    :param name:
    :return:
    '''
    sql = "select code from stock where name = '" + str(name) + "'"
    df = execute_sql(sql)

    if df is not None and len(df) > 0:
        r = df.loc[0, ['code']]
        code = r['code']
        return code
    return


def query_name_by_code(code):
    '''
    根据股票id查股票名
    :param code:
    :return:
    '''
    sql = "select name from stock where code = '" + str(code) + "'"
    df = execute_sql(sql)

    if df is not None and len(df) > 0:
        r = df.loc[0, ['name']]
        name = r['name']
        return name
    return


def query_top(table_name, top=100):
    '''
    读取数据
    :param table_name:
    :param top:
    :return:
    '''
    return execute_sql("select * from '%s' limit %s" % (table_name, top))


def query_all(table_name):
    '''
    获取某表的全部数据
    :param table_name:
    :return:
    '''
    return execute_sql("select * from '%s'" % table_name)


def query_trans_d(code, start_date, end_date=strutils.todayStr()):
    '''
    查询交易数据
    :param code
    :param start_date:
    :param end_date:
    :return:
    '''
    return execute_sql("select * from '%s' where date >= '%s' and date <= '%s' and code = '%s';" % (
    TN_TRANSACTION_D, start_date, end_date, code))
