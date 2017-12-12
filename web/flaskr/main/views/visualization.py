from flask import render_template, make_response
from .. import main
from .data_views import view_trans_d,view_overall_bar

# 创建相关视图
layout = lambda id, name, layout_resp: {"id": id, "name": name, "layout_resp": layout_resp}
view_layout_list = [layout("trans_d", "股票交易记录【每日】", view_trans_d.layout_resp),
                    layout("overall_bar", "总体信息柱状图", view_overall_bar.layout_resp),
                    ]


@main.route('/visualization')
def visualization():
    return make_response(render_template('visualization.html', views=view_layout_list))

@main.route('/visualization/<id>')
def visualization_layout(id):
    for layout in view_layout_list:
        if id == layout['id']:
            return layout['layout_resp']()
    return make_response(render_template('visualization.html', views=view_layout_list))
