import json

import tudata as tu
from flask import request

from .. import main


@main.route('/query/stockNames', methods=['GET'])
def queryStockNames():
    word = request.args.get('word')
    print("query word > %s" % word)

    result = []
    if word:
        sql = "select name, code from stock where name like '%" + str(word) + "%' or code like '%" + str(
            word) + "%' limit 10"
        df = tu.execute_sql(sql)

        if df is not None:
            for i in range(len(df)):
                r = df.loc[i, ['name', 'code']]
                name = r['name']
                code = r['code']
                result.append("%s(%s)" % (name, code))

    return json.dumps(result)
