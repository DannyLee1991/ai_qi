from flask import render_template, make_response
from .. import main
from ...get_data.db import TABLES_INFO_LIST
from ...get_data.db.manager import read_top_data
from ...utils.flash import flash_warning


@main.route('/tables')
def tables():
    resp = make_response(render_template('tables.html', tables=TABLES_INFO_LIST))
    return resp


@main.route('/tables/<table>')
def table_details(table=None):
    df = read_top_data(table)

    if df is not None:
        table = dfData2View(df)
    else:
        flash_warning("表不存在，请确认是否已经拉取过数据")

    resp = make_response(render_template('tables.html', tables=TABLES_INFO_LIST, table=table))
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
