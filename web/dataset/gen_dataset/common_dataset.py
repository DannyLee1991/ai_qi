from ..base import TransDDataSet, TO_TRANS_D
import tudata as tu
import pandas as pd
from utils import strutils
from utils import cache


def gen_trans_d_dataset(name, start_date, end_date=strutils.todayStr(), offset_day=1):
    '''
    生成日交易记录数据集
    :param name: 数据集名称
    :param start_date: 起始日期
    :param end_date: 结束日期
    :param offset_day: Y数据相对于X数据的日期偏差
    :return:
    '''
    des = "开始时间%s,结束时间%s,日期间隔%s" % (start_date, end_date, offset_day)
    dataset = TransDDataSet(TO_TRANS_D,
                            name,
                            pd.DataFrame(),
                            pd.DataFrame(),
                            des,
                            start_date,
                            end_date,
                            offset_day)

    print('开始创建【每日交易记录数据集】')
    print(dataset.info())

    codes = get_trans_d_cache_code(name)

    for index, code in enumerate(tu.all_trans_d_code()):

        if code not in codes:
            dataset.feed(code)
            print("---【%s】执行一次保存操作 x shape %s---" % (dataset.name, dataset.X.shape))
            dataset.save()
            # 记录已获取过的公司，防止重复获取，浪费时间
            set_trans_d_cache_code(name, code)

    print('%s 数据集创建成功' % name)
    return dataset


def get_trans_d_cache_code(name):
    '''
    获取以获取过数据的code缓存
    :return:
    '''
    codes = cache.read_file_cache(cache_file_name(name))
    if not codes:
        codes = []
    return codes


def set_trans_d_cache_code(name, code):
    '''
    用来记录已经获取过的数据的缓存
    :param code:
    :return:
    '''
    c_codes = cache.read_file_cache(cache_file_name(name))
    if c_codes:
        c_codes.append(code)
    else:
        c_codes = [code]
    cache.write_file_cache(cache_file_name(name), c_codes)


def cache_file_name(name):
    return "data_set_%s" % name
