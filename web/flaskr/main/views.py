from flask import render_template, make_response, request, redirect, url_for
from flaskr.utils.flash import *

from . import main
from ..models import History
from ..get_data.db import *
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


@main.route('/fs_data', methods=['GET', 'POST'])
def fs_data():
    t_items = gen_getdata_items()
    what = request.args.get('what')
    params = request.args.get('params')
    if what is not None:
        for item in t_items:
            if item['what'] == what:
                # 执行对应的方法
                if params:
                    item['method'](p['value'] for p in params)
                else:
                    item['method']()
                flash_success("%s 获取成功！" % item['name'])

                History.update_history(what)
    return redirect(url_for('.getdata'))


# ------------

def gen_getdata_items():
    '''
    数据获取 表格数据生成
    :return:
    '''

    item = lambda name, method, what, params=[]: {'name': name,
                                               'params': params,
                                               'method': method,
                                               'what': what,
                                               'history': History.query_history_time(what)
                                               }
    param = lambda name, id, for_what, def_value='', hint='': {'name': name,
                                                               'id': id,
                                                               'for_what': for_what,
                                                               'def_value': def_value,
                                                               'hint': hint
                                                               }

    items = [item(name="【股票基础数据】",
                  method=manager.fs_stock,
                  what=TABLE_STOCK,
                  ),
             item(name="【股票行业数据】",
                  method=manager.fs_stock_industry,
                  what=TABLE_STOCK_INDUSTRY,
                  ),
             item(name="【股票地区数据】",
                  method=manager.fs_stock_area,
                  what=TABLE_STOCK_AREA),
             item(name="【股票概念数据】",
                  method=manager.fs_stock_concept,
                  what=TABLE_STOCK_CONCEPT),

             item(name="【大盘全部股票基本数据】",
                  params=[
                      param(name="日期", id='id_daily', for_what='date', hint="请输入日期"),
                  ],
                  method=manager.fs_stock_basics_daily,
                  what=TABLE_STOCK_BASICS_DAILY),
             ]
    return items
