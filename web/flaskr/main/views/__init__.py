from flaskr.get_data.db.manager import query_code_by_name

def parseQueryStockStr(queryWord):
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