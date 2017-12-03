from flask import render_template, make_response, request, redirect, url_for
from flaskr.utils.flash import *

from . import main
from ..get_data import manager


@main.route('/', methods=['GET', 'POST'])
def index():
    resp = make_response(render_template('index.html'))
    return resp


@main.route('/setting')
def setting():
    resp = make_response(render_template('setting.html'))
    return resp


@main.route('/getdata', methods=['GET'])
def getdata():
    t_items = gen_getdata_items()
    resp = make_response(render_template('getdata.html', t_items=t_items))
    return resp


@main.route('/fs_data', methods=['GET','POST'])
def fs_data():
    t_items = gen_getdata_items()

    what = request.args.get('what')
    if what is not None:
        for item in t_items:
            if item['what'] == what:
                item['method']()
                flash_success("%s 获取成功！" % item['name'])
    return redirect(url_for('.getdata'))

# ------------

def gen_getdata_items():
    '''
    数据获取 表格数据生成
    :return:
    '''

    item = lambda name, params, method, what: {'name': name,
                                               'params': params,
                                               'method': method,
                                               'what': what
                                               }
    items = [item("【股票基础数据】", None, manager.fs_stock, "stock"),
             item("【股票行业数据】", None, manager.fs_stock_industry, "stock_industry"),
             item("【股票地区数据】", None, manager.fs_stock_area, "stock_area"),
             item("【股票概念数据】", None, manager.fs_stock_concept, "stock_concept"),
             ]
    return items
