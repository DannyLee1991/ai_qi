from io import BytesIO
import base64
from flask import make_response, render_template

# 解决matplotlib字体不显示的问题
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def gen_view_data(fig):
    sio = BytesIO()
    fig.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    return data


def make_view_response(plot_method, **kwargs):
    '''
    生成可视化图片相应
    :param plot_method: 绘图所用的方法
    :param kwargs: 绘图所用的参数，用于传递给 plot_method
    :return:
    '''
    data = error = None
    try:
        data, error = plot_method(kwargs)
    except Exception as e:
        error = e
    return make_response(render_template('view_pages/view.html', data=data, error=error))
