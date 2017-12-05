from flask import render_template, make_response, request, redirect, url_for
from flaskr.utils.flash import *

from .. import main
from ...models import History
from ...get_data import manager
from ...utils.strutils import todayStr, perYearStr

@main.route('/getdata', methods=['GET'])
def getdata():
    t_items = gen_getdata_items()
    resp = make_response(render_template('getdata.html', t_items=t_items))
    return resp


@main.route('/fs_data', methods=['POST'])
def fs_data():
    args_dict = request.form.to_dict()
    if args_dict:
        t_items = gen_getdata_items()
        id = args_dict.pop("id")

        params = []
        if args_dict:
            for (k, v) in args_dict.items():
                params.append(v)

        print(type(id))

        for item in t_items:
            if str(item['id']) == id:
                # 执行对应的方法 FIXME 实现方式太蠢，是否有更好的实现呢？
                if params:
                    if len(params) == 4:
                        item['method'](params[0], params[1], params[2], params[3])
                    if len(params) == 3:
                        item['method'](params[0], params[1], params[2])
                    elif len(params) == 2:
                        item['method'](params[0], params[1])
                    elif len(params) == 1:
                        item['method'](params[0])
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
                      param(name='日期', id='id_daily_date', for_what='date', def_value=todayStr(), hint='请输入日期')
                  ],
                  method=manager.fs_stock_basics_daily,
                  ),
             item(id=6,
                  name="【获取大盘指定时间区间内的股票基本数据】",
                  params=[
                      param(name='起始日期', id='id_daily_r_begin_date', for_what='begin_date', def_value=perYearStr(),
                            hint='请输入日期'),
                      param(name='结束日期', id='id_daily_r_end_date', for_what='end_date', def_value=todayStr(),
                            hint='请输入日期')
                  ],
                  method=manager.fs_stock_basics_daily_r,
                  ),
             item(id=7,
                  name="【股票分笔数据】",
                  params=[
                      param(name='股票代码', id='id_tick_code', for_what='code', hint='请输入股票代码'),
                      param(name='日期', id='id_tick_date', for_what='date', def_value=todayStr(), hint='请输入日期')
                  ],
                  method=manager.fs_tick,
                  ),
             item(id=8,
                  name="【指定时间区间内的股票分笔数据】",
                  params=[
                      param(name='股票代码', id='id_tick_code', for_what='code', hint='请输入股票代码'),
                      param(name='起始日期', id='id_tick_r_begin_date', for_what='begin_date', def_value=perYearStr(),
                            hint='请输入日期'),
                      param(name='结束日期', id='id_tick_r_end_date', for_what='end_date', def_value=todayStr(),
                            hint='请输入日期')
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
                      param(name='起始日期', id='id_fuquan_start_date', for_what='start_date', def_value=perYearStr(),
                            hint='请输入日期'),
                      param(name='结束日期', id='id_fuquan_end_date', for_what='end_date', def_value=todayStr(),
                            hint='请输入日期'),
                      param(name='复权类型', id='id_fuquan_autype', for_what='autype', def_value='qfq', hint='qfq/hfq/none')
                  ],
                  method=manager.fs_fuquan,
                  ),
             item(id=14,
                  name="【指定时间区间内的股票复权数据】",
                  params=[
                      param(name='起始日期', id='id_fuquan_all_start_date', for_what='start_date', def_value=perYearStr(),
                            hint='请输入日期'),
                      param(name='结束日期', id='id_fuquan_all_end_date', for_what='end_date', def_value=todayStr(),
                            hint='请输入日期'),
                      param(name='复权类型', id='id_fuquan_all_autype', for_what='autype', def_value='qfq',
                            hint='qfq/hfq/none')
                  ],
                  method=manager.fs_fuquan_all,
                  ),
             ]
    return items
