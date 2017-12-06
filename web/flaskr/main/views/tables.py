from flask import render_template, make_response, request
from .. import main
from ...get_data.db import TABLES_INFO_LIST
from ...get_data.db.manager import read_top_data, query_by_sql
from ...utils.flash import flash_warning


@main.route('/tables')
def tables():
    return make_response(render_template('tables.html', tables=TABLES_INFO_LIST))


@main.route('/tables/<table>')
def table_details(table=None):
    df = read_top_data(table)
    executed_sql = request.cookies.get('executed_sql')

    if df is not None:
        table = dfData2View(df)
    else:
        flash_warning("表不存在，请确认是否已经拉取过数据")

    return make_response(render_template('tables.html', tables=TABLES_INFO_LIST, table=table, executed_sql=executed_sql))


@main.route('/tables/sql', methods=['POST'])
def execute_sql():
    sql = request.form.get('sql')
    title = "查询执行结果"
    table = None

    save = request.form.get('save')

    if sql is None or sql == "":
        title = "查询语句不能为空"
    else:
        df = query_by_sql(sql)
        if df is None:
            title = "没有查到相关数据，请检查您的sql是否正确以及检查相关数据是否已经获取"
        else:
            table = dfData2View(df)

    resp = make_response(render_template('table_layout.html', table=table, title=title, sql=sql))

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
