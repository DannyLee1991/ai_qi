from flask import render_template, make_response, request
from flaskr.get_data.db.handler import query_by_sql, query_name_by_code, create_sql
from ....get_data.db import *
from ....get_data.db.handler import column_names, SqlWhereIs, SqlWhereRange
from ... import main
from .. import parseQueryStockStr
from . import gen_view_data
from flaskr.utils.strutils import perYearStr, todayStr


def trans_d_layout_resp():
    '''
    获取日交易数据操作界面的布局相应对象
    :return:
    '''
    columns = column_names(TN_TRANSACTION_D)
    if columns:
        columns.remove('date')
        columns.remove('code')
    date = {'start': perYearStr(), 'end': todayStr()}
    resp = make_response(render_template('views/layout_trans_d.html', columns=columns, date=date))
    return resp


@main.route('/views/view_trans_d', methods=['POST'])
def view_trans_d():
    '''
    生成日交易数据视图
    :return:
    '''
    queryWord = request.form.get('queryWord')
    which = request.form.get('which')
    start = request.form.get('start')
    end = request.form.get('end')
    if which:
        which = list(which[:-1].split(','))
    else:
        which = "open"

    code = parseQueryStockStr(queryWord)
    data = error = None
    try:
        stock_name = query_name_by_code(code)
        name = "%s(%s) 日交易记录" % (stock_name, code)
        data = gen_trans_d_view_data(name, code, which=which, date_start=start, date_end=end)
    except Exception as e:
        print(e)
        error = e
    return make_response(render_template('views/view.html', data=data, error=error))


def gen_trans_d_view_data(view_name, code, which, date_start, date_end):
    '''
    生成每日交易数据的视图数据
    :param name:
    :param which:
    :return:
    '''
    fig = plot_transaction_d(view_name, code, which, date_start, date_end)
    return gen_view_data(fig)


def plot_transaction_d(view_name, code, which, date_start, date_end, limit=-1):
    '''
    绘制 股票交易记录数据 【每日】
    :param name:
    :return:
    '''
    if "date" not in which:
        which.append("date")

    where_is_list = [SqlWhereIs('code', code), ]
    where_range_list = [SqlWhereRange('date', date_start, date_end), ]

    sql = create_sql(TN_TRANSACTION_D, which, "date", limit,
                     where_is_list=where_is_list,
                     where_range_list=where_range_list
                     )
    df = query_by_sql(sql)
    df.cumsum(0)
    plot = df.plot(x='date', title=view_name)
    fig = plot.get_figure()
    return fig
