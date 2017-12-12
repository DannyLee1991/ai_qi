from flask import render_template, make_response
from .. import main
from .data_views import view_trans_d,view_overall_bar

# 创建相关视图
layout = lambda id, name, resp: {"id": id, "name": name, "resp": resp}
view_pages = [layout("trans_d", "股票交易记录【每日】", view_trans_d.resp),
              layout("overall_bar", "总体信息柱状图", view_overall_bar.resp),
              ]


@main.route('/visualization')
def visualization():
    return make_response(render_template('visualization.html', views=view_pages))

@main.route('/visualization/<id>')
def visualization_layout(id):
    for page in view_pages:
        if id == page['id']:
            return page['resp'](view_pages)
    return make_response(render_template('visualization.html', views=view_pages))
