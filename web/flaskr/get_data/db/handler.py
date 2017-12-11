from sqlalchemy import VARCHAR
import pandas as pd
from sqlalchemy.exc import OperationalError

from . import *


def write2db(df, table, if_exists):
    '''
    写入db
    :param df:
    :return:
    '''
    if df is not None:
        index_name = df.index.name
        dtype = {}
        if index_name:
            dtype[index_name] = VARCHAR(df.index.get_level_values(index_name).str.len().max())

        df.to_sql(table, engine, if_exists=if_exists, dtype=dtype)
        print("新数据插入成功 [table: %s ]" % (table))
    else:
        print("数据异常 没有数据入库")


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


def read_top_data(table, top=100):
    '''
    读取数据
    :param table:
    :param top:
    :return:
    '''
    try:
        df = pd.read_sql("select * from '%s' limit %s" % (table, top), engine)
    except OperationalError:
        df = None
    return df


def query_by_sql(sql):
    '''
    根据sql查询数据
    :param sql:
    :return:
    '''
    try:
        print("sql > %s" % sql)
        df = pd.read_sql(sql, engine)
    except OperationalError:
        df = None
    return df


def query_code_by_name(name):
    '''
    根据股票名称查询id
    :param name:
    :return:
    '''
    sql = "select code from stock where name = '" + str(name) + "'"
    df = query_by_sql(sql)

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
    df = query_by_sql(sql)

    if df is not None and len(df) > 0:
        r = df.loc[0, ['name']]
        name = r['name']
        return name
    return

def column_label(column):
    '''
    根据列名 获取对应的标签名
    :param column:
    :return:
    '''
    return COLUMN_LABEL_DICT[column]

def column_names(table_name):
    '''
    获取表的列名
    :param table_name:
    :return:
    '''
    df = query_by_sql("select * from %s limit 1" % table_name)
    if df is not None:
        columns = [column for column in df]
        return columns
    return None


# -----------

SqlWhereIs = lambda name, val: {'name': name, 'val': val}
SqlWhereRange = lambda name, start='', end='': {'name': name, 'start': start, 'end': end}
SqlAnd = ' and '
SqlEq = lambda name, value: " %s = '%s' " % (name, value)
SqlGe = lambda name, value: " %s >= '%s' " % (name, value)
SqlLe = lambda name, value: " %s <= '%s' " % (name, value)


def create_sql(table, which, orderby, limit, **kwargs):
    '''
    构造sql
    :param table:
    :param which:
    :param limit:
    :return:
    '''
    which_sql = gen_which_sql_str(which)
    limit_sql = str(limit) if limit > 0 else ""

    where_is_list = kwargs['where_is_list']
    where_range_list = kwargs['where_range_list']
    where_sql = gen_where_sql(where_is_list, where_range_list)

    sql = "select %s from %s %s order by %s %s" % (which_sql, table, where_sql, orderby, limit_sql)
    print("create sql > %s" % sql)
    return sql


def gen_where_sql(where_is_list, where_range_list):
    '''
    生成where部分的sql语句
    :param where_is_list:
    :return:
    '''
    where_sql = ""
    if where_is_list or where_range_list:

        # 生成equals sql逻辑
        equals_sql = ''
        for index, where_is in enumerate(where_is_list):
            is_sql = SqlEq(where_is['name'], where_is['val'])
            if index < len(where_is_list) - 1:
                is_sql += SqlAnd
            equals_sql += is_sql

        # 生成range sql逻辑
        range_sql = ''
        for where_range in where_range_list:
            r_name = where_range['name']
            r_start = where_range['start']
            r_end = where_range['end']

            start_sql = end_sql = ''
            if r_start:
                start_sql = SqlGe(r_name, r_start)
            if r_end:
                end_sql = SqlLe(r_name, r_end)
            if start_sql and end_sql:
                range_sql += start_sql + SqlAnd + end_sql
            else:
                range_sql += start_sql + end_sql

        where_sql = "where"
        if equals_sql and range_sql:
            where_sql += equals_sql + SqlAnd + range_sql
        else:
            where_sql += equals_sql + range_sql

    print("gen where sql > %s" % where_sql)
    return where_sql


def gen_which_sql_str(which):
    '''
    根据元组参数 生成sql查询语句的which部分
    :param which:
    :return:
    '''
    sql = "*"
    if which:
        if type(which) is str:
            sql = which
        else:
            sql = ""
            for s in which:
                sql += s + ","
            sql = sql[:-1]
    return sql
