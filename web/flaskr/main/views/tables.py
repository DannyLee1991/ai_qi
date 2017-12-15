import tudata as tu
from flask import render_template, make_response, request

from .. import main


@main.route('/tables')
def tables():
    return make_response(render_template('tables.html', tables=tu.TABLE_LIST))

@main.route('/tables/sql', methods=['POST'])
def execute_sql():
    sql = request.form.get('sql')
    title = "查询执行结果"
    table_body = None
    count = None

    save = request.form.get('save')

    if sql is None or sql == "":
        title = "查询语句不能为空"
    else:
        df = tu.read_sql(sql)
        if df is None:
            title = "没有查到相关数据，请检查您的sql是否正确以及检查相关数据是否已经获取"
        else:
            table_body = dfData2View(df)
            count = len(df)

    resp = make_response(render_template('tables/table_layout.html', table_body=table_body, title=title,count=count, sql=sql))

    # 保存sql
    if save and str(save).lower() == "true":
        resp.set_cookie('executed_sql', sql)
    return resp


def dfData2View(df):
    '''
    将pandas DataFrame 的数据转换成前台界面可以显示的格式
    :param df:
    :return:
    '''
    # 获取列明
    th = [column for column in df]
    tb = []
    # 获取每一行数据
    for i in range(len(df)):
        l = df.iloc[i, :]
        tb.append([l[c] for c in th])
    return {"th": th, "tb": tb}
