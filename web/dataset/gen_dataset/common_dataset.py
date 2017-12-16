from ..base import DataSet, TO_TRANS_D
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
    print('开始创建【每日交易记录数据集】')
    print('-- name => %s ' % name)
    print('-- start_date => %s ' % start_date)
    print('-- end_date => %s ' % end_date)
    print('-- offset_day => %s ' % offset_day)

    X = pd.DataFrame()
    Y = pd.DataFrame()

    des = "开始时间%s,结束时间%s,日期间隔%s" % (start_date, end_date, offset_day)
    dataset = DataSet(TO_TRANS_D, name, X, Y, des)

    for index, code in enumerate(tu.all_trans_d_code()):
        df = tu.query_trans_d(code, start_date, end_date)
        # 由于涨跌幅是次日的  所以要对数据进行'错位' 并且'错位之后'对X剔除末尾行，对Y剔除首行
        x = df[:-offset_day]
        y = pd.DataFrame({'p_change': df['p_change']})[offset_day:]

        if len(X) > 0:
            X = X.append(x, ignore_index=True)
        else:
            X = x

        if len(Y) > 0:
            Y = Y.append(y, ignore_index=True)
        else:
            Y = y

        # 为尽量保证数据不丢失 每100步 存一次
        if index % 10 == 0:
            print("---【%s】执行一次保存操作 x shape %s---" % (name, X.shape))
            dataset.save()

    dataset.save()

    print('%s 数据集创建成功' % name)
    return dataset
