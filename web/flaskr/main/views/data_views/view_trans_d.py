import tudata as tu
from flask import render_template, make_response, request
from utils.strutils import perYearStr, todayStr
import pandas as pd

from . import gen_view_data, make_view_response
from ... import main


def resp(views):
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
    return make_response(render_template('view_pages/page_trans_d.html', views=views, columns=columns, date=date))


@main.route('/views/view_trans_d', methods=['POST'])
def view_trans_d():
    '''
    生成日交易数据视图
    :return:
    '''
    queryWords = request.form.get('queryWords')
    which = request.form.get('which')
    start = request.form.get('start')
    end = request.form.get('end')
    if which:
        which = list(which[:-1].split(','))
    else:
        which = "open"
    if queryWords:
        queryWords = list(queryWords[:-1].split(','))

    codes = []
    for word in queryWords:
        code = tu.queryCode(word)
        if code:
            codes.append(code)

    return make_view_response(plot_trans_d, codes=codes, which=which, date_start=start, date_end=end)


def plot_trans_d(kwargs):
    '''
    绘制 股票交易记录数据 【每日】
    :param kwargs: 绘图相关参数
    :return:
    '''

    codes = kwargs['codes']
    which = kwargs['which']
    date_start = kwargs['date_start']
    date_end = kwargs['date_end']
    limit = -1

    name = "日交易记录"

    error = ""
    df = None
    for code in codes:
        stock_name = tu.query_name_by_code(code)

        which_as_prefix = "%s(%s)_" % (stock_name, code)
        sql = make_sql(code, date_end, date_start, limit, which, which_as_prefix=which_as_prefix)
        _df = tu.execute_sql(sql)
        if len(_df) > 0:
            if df is not None:
                df = pd.merge(df, _df, on='date')
                print(df)
            else:
                df = _df
        else:
            error = "%s(%s) 的数据不存在，请检查是否已获取" % (stock_name, code)

    if df is not None:
        df.cumsum(0)
        plot = df.plot(x='date', title=name)
        fig = plot.get_figure()

        data = gen_view_data(fig)
    else:
        data = None
        error = "查询结果为空，请检查输入是否有误"
    return data, error


def make_sql(code, date_end, date_start, limit, which, which_as_prefix=''):
    if "date" not in which:
        which.append("date")
    where_is_list = [tu.SqlWhereIs('code', code), ]
    where_range_list = [tu.SqlWhereRange('date', date_start, date_end), ]
    sql = tu.create_sql(tu.TN_TRANSACTION_D, which, "date", limit,
                        where_is_list=where_is_list,
                        where_range_list=where_range_list,
                        which_as_prefix=which_as_prefix,
                        which_no_prefix='date'
                        )
    return sql
