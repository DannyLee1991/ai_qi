from flask import render_template, make_response, request, redirect, url_for
from flaskr.utils.flash import *
import json

from . import main
from ..models import History
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
    if request.args:
        t_items = gen_getdata_items()
        id = int(request.args.get('id'))
        params = json.loads(request.args.get('params'))

        for item in t_items:
            if item['id'] == id:
                # 执行对应的方法 FIXME 实现方式太蠢，是否有更好的实现呢？
                if len(params) == 4:
                    item['method'](params[0]['value'], params[1]['value'], params[2]['value'], params[3]['value'])
                if len(params) == 3:
                    item['method'](params[0]['value'], params[1]['value'], params[2]['value'])
                elif len(params) == 2:
                    item['method'](params[0]['value'], params[1]['value'])
                elif len(params) == 1:
                    item['method'](params[0]['value'])
                else:
                    item['method']()
                flash_success("%s 获取成功！" % item['name'])

                History.update_history(id)
    return redirect(url_for('.getdata'))


# ------------

def gen_getdata_items():
    '''
    数据获取 表格数据生成
    :return:
    '''

    item = lambda id, name, method, params=[]: {'id': id,
                                                      'name': name,
                                                      'params': params,
                                                      'method': method,
                                                      'history': History.query_history_time(id),
                                                      'param_ids': [param['id'] for param in params]
                                                      }
    param = lambda name, id, for_what, def_value='', hint='': {'name': name,
                                                               'id': id,
                                                               'for_what': for_what,
                                                               'def_value': def_value,
                                                               'hint': hint
                                                               }

    items = [item(id=1,
                  name="【股票基础数据】",
                  method=manager.fs_stock,
                  ),
             item(id=2,
                  name="【股票行业数据】",
                  method=manager.fs_stock_industry,
                  ),
             item(id=3,
                  name="【股票地区数据】",
                  method=manager.fs_stock_area,
                  ),
             item(id=4,
                  name="【股票概念数据】",
                  method=manager.fs_stock_concept,
                  ),

             item(id=5,
                  name="【大盘全部股票基本数据】",
                  params=[
                      param(name='日期', id='id_daily_date', for_what='date', hint='请输入日期')
                  ],
                  method=manager.fs_stock_basics_daily,
                  ),
             item(id=6,
                  name="【获取大盘指定时间区间内的股票基本数据】",
                  params=[
                      param(name='起始日期', id='id_daily_r_begin_date', for_what='begin_date', hint='请输入日期'),
                      param(name='结束日期', id='id_daily_r_end_date', for_what='end_date', hint='请输入日期')
                  ],
                  method=manager.fs_stock_basics_daily_r,
                  ),
             item(id=7,
                  name="【股票分笔数据】",
                  params=[
                      param(name='股票代码', id='id_tick_code', for_what='code', hint='请输入股票代码'),
                      param(name='日期', id='id_tick_date', for_what='date', hint='请输入日期')
                  ],
                  method=manager.fs_tick,
                  ),
             item(id=8,
                  name="【指定时间区间内的股票分笔数据】",
                  params=[
                      param(name='股票代码', id='id_tick_code', for_what='code', hint='请输入股票代码'),
                      param(name='起始日期', id='id_tick_r_begin_date', for_what='begin_date', hint='请输入日期'),
                      param(name='结束日期', id='id_tick_r_end_date', for_what='end_date', hint='请输入日期')
                  ],
                  method=manager.fs_tick_r,
                  ),
             item(id=9,
                  name="【股票最新的日交易数据】",
                  params=[
                      param(name='股票代码', id='id_transaction_d_code', for_what='code', hint='请输入股票代码')
                  ],
                  method=manager.fs_transaction_d,
                  ),
             item(id=10,
                  name="【股票最新的5分钟交易数据】",
                  params=[
                      param(name='股票代码', id='id_transaction_5min_code', for_what='code', hint='请输入股票代码')
                  ],
                  method=manager.fs_transaction_5min,
                  ),
             item(id=11,
                  name="【全部股票的最新的日交易数据】",
                  method=manager.fs_transaction_d_all,
                  ),
             item(id=12,
                  name="【全部股票的最新的5分钟交易数据】",
                  method=manager.fs_transaction_5min_all,
                  ),
             item(id=13,
                  name="【股票复权数据】",
                  params=[
                      param(name='股票代码', id='id_fuquan_code', for_what='code', hint='请输入股票代码'),
                      param(name='起始日期', id='id_fuquan_start_date', for_what='start_date', hint='请输入日期'),
                      param(name='结束日期', id='id_fuquan_end_date', for_what='end_date', hint='请输入日期'),
                      param(name='复权类型', id='id_fuquan_autype', for_what='autype', hint='qfq/hfq/none')
                  ],
                  method=manager.fs_fuquan,
                  ),
             item(id=14,
                  name="【指定时间区间内的股票复权数据】",
                  params=[
                      param(name='起始日期', id='id_fuquan_all_start_date', for_what='start_date', hint='请输入日期'),
                      param(name='结束日期', id='id_fuquan_all_end_date', for_what='end_date', hint='请输入日期'),
                      param(name='复权类型', id='id_fuquan_all_autype', for_what='autype', hint='qfq/hfq/none')
                  ],
                  method=manager.fs_fuquan_all,
                  ),
             ]
    return items
