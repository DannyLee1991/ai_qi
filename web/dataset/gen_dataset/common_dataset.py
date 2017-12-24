from ..base import TransDDataSet, TO_TRANS_D
import pandas as pd
from utils import strutils


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
    return TransDDataSet(TO_TRANS_D,
                         name,
                         pd.DataFrame(),
                         pd.DataFrame(),
                         des,
                         start_date,
                         end_date,
                         offset_day)
