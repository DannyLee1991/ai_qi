from sqlalchemy import VARCHAR
from ...utils.cache import cache
from ..db import *
from sqlalchemy.exc import OperationalError

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