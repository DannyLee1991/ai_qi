from flask import render_template, make_response, request
from flaskr.get_data.db.handler import query_by_sql, query_name_by_code, create_sql
from ....get_data.db import *
from ....get_data.db.handler import column_names, column_label, SqlWhereIs, SqlWhereRange
from ... import main
from .. import parseQueryStockStr
from . import gen_view_data, make_view_response
from flaskr.utils.strutils import perYearStr, todayStr


def layout_resp():
    '''
    获取日交易数据操作界面的布局相应对象
    :return:
    '''
    c_names = column_names(TN_TRANSACTION_D)
    columns = []
    if c_names:
        c_names.remove('date')
        c_names.remove('code')
        for name in c_names:
            label = column_label(name)
            columns.append({'name': name, 'label': label})

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

    return make_view_response(plot_trans_d, code=code, which=which, date_start=start, date_end=end)


def plot_trans_d(kwargs):
    '''
    绘制 股票交易记录数据 【每日】
    :param name:
    :param which:
    :return:
    '''

    code = kwargs['code']
    which = kwargs['which']
    date_start = kwargs['date_start']
    date_end = kwargs['date_end']
    limit = -1

    stock_name = query_name_by_code(code)
    name = "%s(%s) 日交易记录" % (stock_name, code)

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
    plot = df.plot(x='date', title=name)
    fig = plot.get_figure()

    data = gen_view_data(fig)
    return data
