def sql_delete_duplicate_data(table_name, *fields):
    # 由于pandas写入db，只有三种形式 append，replace，fail
    # 这三种方法都无法实现不添加重复数据，所以需要在插入数据结束之后 清理一下db的重复数据
    '''
    删除重复数据的sql
    :param table_name:
    :param fields:
    :return:
    '''

    # eg : "field1,field2"
    fields_str = ""
    for field in fields:
        fields_str += str(field) + ","
    if fields_str:
        fields_str = fields_str[:-1]

    sql = "delete from %(table_name)s where " \
          "(%(fields)s) in (select %(fields)s from %(table_name)s group by %(fields)s having count(*) > 1)" \
          " and rowid not in (select min(rowid) " \
          "from %(table_name)s group by %(fields)s having count(*)>1)" % \
          {'table_name': table_name, 'fields': fields_str}
    print("sql >> %s" % sql)
    return sql
