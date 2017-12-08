from io import BytesIO
import base64
from flask import render_template, make_response, request
from flaskr.get_data.db.manager import query_by_sql, query_code_by_name, query_name_by_code, create_sql
from ...get_data.db import *
from .. import main

# 解决matplotlib字体不显示的问题
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 创建相关视图
layout = lambda id, name: {"id": id, "name": name}
view_layout_list = [layout("trans_d", "交易数据【每日】"), ]


@main.route('/visualization')
def visualization():
    return make_response(render_template('visualization.html', views=view_layout_list))


@main.route('/views/layout', methods=['POST'])
def view_layout():
    '''
    生成视图
    :return:
    '''
    layout_id = request.form.get('layout_id')
    for layout in view_layout_list:
        if layout_id == layout['id']:
            # 获取transaction_d表的列名
            df = query_by_sql("select * from transaction_d limit 1")
            columns = [column for column in df]
            columns.remove('date')
            columns.remove('code')
            return make_response(render_template('views/layout_trans_d.html', columns=columns))


@main.route('/views/view_trans_d', methods=['POST'])
def view_trans_d():
    '''
    生成日交易数据视图
    :return:
    '''
    queryWord = request.form.get('queryWord')
    which = request.form.get('which')
    if which:
        which = list(which[:-1].split(','))
    else:
        which = "open"

    code = parseQueryStockStr(queryWord)
    data = error = None
    try:
        stock_name = query_name_by_code(code)
        name = "%s(%s) 日交易记录" % (stock_name, code)
        data = gen_trans_d_view_data(name, code, which=which)
    except:
        error = "数据有误，可能是对应股票的数据未获取到，请排查"
    return make_response(render_template('views/view.html', data=data, error=error))


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


def gen_trans_d_view_data(view_name, code, which):
    '''
    生成每日交易数据的视图数据
    :param name:
    :param which:
    :return:
    '''
    fig = plot_transaction_d(view_name, code, which=which)
    return gen_view_data(fig)


def gen_view_data(fig):
    sio = BytesIO()
    fig.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    return data


def plot_transaction_d(view_name, code, which, limit=-1):
    '''
    绘制 股票交易记录数据 【每日】
    :param name:
    :return:
    '''
    if "date" not in which:
        which.append("date")
    sql = create_sql(TABLE_TRANSACTION_D, which, "code", code, "date", limit)
    df = query_by_sql(sql)
    df.cumsum(0)
    plot = df.plot(x='date', title=view_name)
    fig = plot.get_figure()
    return fig
