import tudata as tu
from flask import render_template, make_response, request
from utils.strutils import perYearStr, todayStr

from . import gen_view_data, make_view_response
from ... import main


def layout_resp():
    '''
    获取日交易数据操作界面的布局相应对象
    :return:
    '''
    c_names = tu.column_names(tu.TN_TRANSACTION_D)
    columns = []
    if c_names:
        c_names.remove('date')
        c_names.remove('code')
        for name in c_names:
            label = tu.column_label(name)
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

    code = tu.parseQueryStockStr(queryWord)

    return make_view_response(plot_trans_d, code=code, which=which, date_start=start, date_end=end)


def plot_trans_d(kwargs):
    '''
    绘制 股票交易记录数据 【每日】
    :param kwargs: 绘图相关参数
    :return:
    '''

    code = kwargs['code']
    which = kwargs['which']
    date_start = kwargs['date_start']
    date_end = kwargs['date_end']
    limit = -1

    stock_name = tu.query_name_by_code(code)
    name = "%s(%s) 日交易记录" % (stock_name, code)

    if "date" not in which:
        which.append("date")

    where_is_list = [tu.SqlWhereIs('code', code), ]
    where_range_list = [tu.SqlWhereRange('date', date_start, date_end), ]

    sql = tu.create_sql(tu.TN_TRANSACTION_D, which, "date", limit,
                     where_is_list=where_is_list,
                     where_range_list=where_range_list
                     )
    df = tu.execute_sql(sql)
    df.cumsum(0)
    plot = df.plot(x='date', title=name)
    fig = plot.get_figure()

    data = gen_view_data(fig)
    return data
