from ..base import TransDDataSet, TO_TRANS_D
import tudata as tu
import pandas as pd
from utils import strutils
from ..get_dataset import get_dataset


def gen_trans_d_dataset(name, start_date, end_date=strutils.todayStr(), offset_day=1):
    '''
    生成日交易记录数据集
    :param name: 数据集名称
    :param start_date: 起始日期
    :param end_date: 结束日期
    :param offset_day: Y数据相对于X数据的日期偏差
    :return:
    '''

    dataset = load_or_create(end_date, name, offset_day, start_date)

    print('开始创建【每日交易记录数据集】')
    print(dataset.info())

    for index, code in enumerate(tu.all_trans_d_code()):
        dataset.feed(code)
        print("---【%s】执行一次保存操作 x shape %s---" % (dataset.name, dataset.X.shape))
        dataset.save()

    print('%s 数据集创建成功' % name)
    return dataset


def load_or_create(end_date, name, offset_day, start_date):
    dataset = get_dataset(TO_TRANS_D['type'], name)
    if not dataset:
        des = "开始时间%s,结束时间%s,日期间隔%s" % (start_date, end_date, offset_day)
        dataset = TransDDataSet(TO_TRANS_D,
                                name,
                                pd.DataFrame(),
                                pd.DataFrame(),
                                des,
                                start_date,
                                end_date,
                                offset_day)
    return dataset
