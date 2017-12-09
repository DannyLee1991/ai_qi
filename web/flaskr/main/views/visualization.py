from flask import render_template, make_response, request
from .. import main
from .data_views.trans_d import trans_d_layout_resp

# 创建相关视图
layout = lambda id, name, layout_resp: {"id": id, "name": name, "layout_resp": layout_resp}
view_layout_list = [layout("trans_d", "股票交易记录【每日】", trans_d_layout_resp), ]


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
