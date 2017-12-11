from flask import render_template, make_response, request, redirect, url_for
from flaskr.utils.flash import *
from flaskr.get_data.db.handler import *
from flaskr.get_data import manager

from .. import main
from ...models import History
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
                if k == 'nameCode':
                    v = parseQueryStockStr(v)
                params.append(v)

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

getdata_form = lambda id, name, table, method, params=[]: {'id': id,
                                                            'name': name,
                                                            'table': table,
                                                            'params': params,
                                                            'method': method,
                                                            'history': History.query_history_time(id),
                                                            'param_names': [param['name'] for param in params]
                                                            }

param = lambda label, name, def_value='', hint='', type='': {'label': label,
                                                             'name': name,
                                                             'def_value': def_value,
                                                             'hint': hint,
                                                             'type': type
                                                             }


def gen_getdata_items():
    '''
    数据获取 表格数据生成
    :return:
    '''

    items = [getdata_form(id=1,
                          name="【股票基础数据】",
                          table=T_STOCK,
                          method=manager.fs_stock,
                          ),
             getdata_form(id=2,
                          name="【股票行业数据】",
                          table=T_STOCK_INDUSTRY,
                          method=manager.fs_stock_industry,
                          ),
             getdata_form(id=3,
                          name="【股票地区数据】",
                          table=T_STOCK_AREA,
                          method=manager.fs_stock_area,
                          ),
             getdata_form(id=4,
                          name="【股票概念数据】",
                          table=T_STOCK_CONCEPT,
                          method=manager.fs_stock_concept,
                          ),

             getdata_form(id=5,
                          name="【大盘全部股票基本数据】",
                          table=T_STOCK_BASICS_DAILY,
                          params=[
                              param(label='日期', name='date', def_value=todayStr(), hint='请输入日期',
                                    type="date")
                          ],
                          method=manager.fs_stock_basics_daily,
                          ),
             getdata_form(id=6,
                          name="【获取大盘指定时间区间内的股票基本数据】",
                          table=T_STOCK_BASICS_DAILY,
                          params=[
                              param(label='起始日期', name='begin_date', def_value=perYearStr(),
                                    hint='请输入日期', type="date"),
                              param(label='结束日期', name='end_date', def_value=todayStr(),
                                    hint='请输入日期', type="date")
                          ],
                          method=manager.fs_stock_basics_daily_r,
                          ),
             getdata_form(id=7,
                          name="【股票分笔数据】",
                          table=T_TICK,
                          params=[
                              param(label='股票代码', name='nameCode', hint='请输入股票代码', type='stock'),
                              param(label='日期', name='date', def_value=todayStr(), hint='请输入日期',
                                    type="date")
                          ],
                          method=manager.fs_tick,
                          ),
             getdata_form(id=8,
                          name="【指定时间区间内的股票分笔数据】",
                          table=T_TICK,
                          params=[
                              param(label='股票代码', name='nameCode', hint='请输入股票代码', type='stock'),
                              param(label='起始日期', name='begin_date', def_value=perYearStr(),
                                    hint='请输入日期', type="date"),
                              param(label='结束日期', name='end_date', def_value=todayStr(),
                                    hint='请输入日期', type="date")
                          ],
                          method=manager.fs_tick_r,
                          ),
             getdata_form(id=9,
                          name="【股票最新的日交易数据】",
                          table=T_TRANSACTION_D,
                          params=[
                              param(label='股票代码', name='nameCode', hint='请输入股票代码', type='stock')
                          ],
                          method=manager.fs_transaction_d,
                          ),
             getdata_form(id=10,
                          name="【股票最新的5分钟交易数据】",
                          table=T_TRANSACTION_5MIN,
                          params=[
                              param(label='股票代码', name='nameCode', hint='请输入股票代码', type='stock')
                          ],
                          method=manager.fs_transaction_5min,
                          ),
             getdata_form(id=11,
                          name="【全部股票的最新的日交易数据】",
                          table=T_TRANSACTION_D,
                          method=manager.fs_transaction_d_all,
                          ),
             getdata_form(id=12,
                          name="【全部股票的最新的5分钟交易数据】",
                          table=T_TRANSACTION_5MIN,
                          method=manager.fs_transaction_5min_all,
                          ),
             getdata_form(id=13,
                          name="【股票复权数据】",
                          table=T_FUQUAN,
                          params=[
                              param(label='股票代码', name='nameCode', hint='请输入股票代码', type='stock'),
                              param(label='起始日期', name='start_date', def_value=perYearStr(),
                                    hint='请输入日期', type="date"),
                              param(label='结束日期', name='end_date', def_value=todayStr(),
                                    hint='请输入日期', type="date"),
                              param(label='复权类型', name='autype', def_value='qfq', hint='qfq/hfq/none')
                          ],
                          method=manager.fs_fuquan,
                          ),
             getdata_form(id=14,
                          name="【指定时间区间内的股票复权数据】",
                          table=T_FUQUAN,
                          params=[
                              param(label='起始日期', name='start_date', def_value=perYearStr(),
                                    hint='请输入日期', type="date"),
                              param(label='结束日期', name='end_date', def_value=todayStr(),
                                    hint='请输入日期', type="date"),
                              param(label='复权类型', name='autype', def_value='qfq',
                                    hint='qfq/hfq/none')
                          ],
                          method=manager.fs_fuquan_all,
                          ),
             ]
    return items
