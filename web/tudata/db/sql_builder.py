'''
sql 构造器   通过传参的方式来构造sql语句
'''

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
    which_as_prefix = kwargs['which_as_prefix']
    # 没有前缀的列
    which_no_prefix = kwargs['which_no_prefix']
    which_sql = gen_which_sql_str(which, which_as_prefix,which_no_prefix)
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


def gen_which_sql_str(which, which_as_prefix='',which_no_prefix=''):
    '''
    根据元组参数 生成sql查询语句的which部分
    :param which:
    :return:
    '''
    sql = "*"
    # 指定 如果没有前缀 则不添加 as 语句  如果有前缀 则添加 as which_no_prefix+col_name
    as_sql = lambda s: "" if s == which_no_prefix else " as '%s%s' " % (which_as_prefix, s)

    if which:
        if type(which) is str:
            sql = which + as_sql(which)
        else:
            sql = ""
            for s in which:
                sql += s + as_sql(s) + ","
            sql = sql[:-1]
    return sql
