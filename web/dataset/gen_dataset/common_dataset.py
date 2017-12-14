from ..base import DataSet
import tudata as tu
import pandas as pd
from utils import strutils


def gen_trans_d_dataset(name, start_date, end_date=strutils.todayStr(), offset_day=1):
    '''
    生成日交易记录数据集
    :param name: 数据集名称
    :param start_date:
    :param end_date:
    :param offset_day:
    :return:
    '''
    X = None
    Y = None

    for code in tu.all_trans_d_code():
        df = tu.query_trans_d(code, start_date, end_date)
        # 由于涨跌幅是次日的  所以要对数据进行'错位' 并且'错位之后'对X剔除末尾行，对Y剔除首行
        x = df[:-offset_day]
        y = pd.DataFrame({'p_change': df['p_change']})[offset_day:]

        if X is not None:
            X.append(x)
        else:
            X = x

        if Y is not None:
            Y.append(y)
        else:
            Y = y

    info = "开始时间%s,结束时间%s,日期间隔%s" % (start_date, end_date, offset_day)
    dataset = DataSet(X, Y, name, info)
    dataset.save()
    return dataset
