import matplotlib.pyplot as plt
import tudata as tu
from flask import render_template, make_response, request

from . import gen_view_data, make_view_response
from ... import main

bar_type = lambda id, name: {'id': id, 'name': name}

bar_type_list = [
    bar_type('industry', '行业分布'),
    bar_type('area', '地区分布'),
    bar_type('concept', '概念分布'),
]


def resp(views):
    resp = make_response(render_template('view_pages/page_overall_bar.html', views=views, bar_type_list=bar_type_list))
    return resp


@main.route('/views/view_overall_bar', methods=['POST'])
def view_overall_bar():
    type = request.form.get('type')
    limit = request.form.get('limit')
    return make_view_response(plot_overall_bar, type=type, limit=limit)


def plot_overall_bar(kargs):
    '''
    绘制 股票交易记录数据 【每日】
    :param name:
    :return:
    '''
    type = kargs['type']
    limit = kargs['limit']

    plot = gen_plot(type, limit)

    fig = plot.get_figure()

    plt.ylabel('公司数量')
    # 由于字体显示太大  导致显示不完全，所以需要重新设置x轴标签字体大小
    # 参考此博文 [https://www.cnblogs.com/Qwells/p/6215280.html]
    plt.xticks(fontsize=7)

    data = gen_view_data(fig)
    error = ""
    return data, error


def gen_plot(type, limit):
    plot = gen_industry_plot(limit)

    if type == 'industry':
        plot = gen_industry_plot(limit)
    elif type == 'area':
        plot = gen_area_plot(limit)
    elif type == 'concept':
        plot = gen_concept_plot(limit)
    return plot


def gen_industry_plot(limit):
    sql = "select count(*) as count,c_name from stock_industry group by c_name order by count desc limit %s" % (limit)
    df = tu.execute_sql(sql)
    df.cumsum(0)
    plot = df.plot(x='c_name', title="公司行业分布", kind='bar')
    return plot


def gen_area_plot(limit):
    sql = "select count(*) as count,area from stock_area group by area order by count desc limit %s" % (limit)
    df = tu.execute_sql(sql)
    df.cumsum(0)
    plot = df.plot(x='area', title="公司地区分布", kind='bar')
    return plot


def gen_concept_plot(limit):
    sql = "select count(*) as count,c_name from stock_concept group by c_name order by count desc limit %s" % (limit)
    df = tu.execute_sql(sql)
    df.cumsum(0)
    plot = df.plot(x='c_name', title="公司概念分布", kind='bar')
    return plot
