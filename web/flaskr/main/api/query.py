from flask import render_template, make_response, request
from .. import main
import json
from ...get_data.db.manager import query_by_sql


@main.route('/query/stockNames', methods=['GET'])
def queryStockNames():
    word = request.args.get('word')
    print("query word > %s" % word)

    result = []
    if word:
        sql = "select name, code from stock where name like '%" + str(word) + "%' or code like '%" + str(
            word) + "%' limit 10"
        df = query_by_sql(sql)

        if df is not None:
            for i in range(len(df)):
                r = df.loc[i, ['name', 'code']]
                name = r['name']
                code = r['code']
                result.append("%s(%s)" % (name, code))

    return json.dumps(result)
