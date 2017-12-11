from flask import render_template, make_response, request
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


@main.route('/views/layout', methods=['POST'])
def view_layout():
    '''
    生成视图
    :return:
    '''
    layout_id = request.form.get('layout_id')
    for layout in view_layout_list:
        if layout_id == layout['id']:
            return layout['layout_resp']()
