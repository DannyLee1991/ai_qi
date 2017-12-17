import dataset as ds
import tudata as tu
import pandas as pd
import numpy as np
import random

#
# #
# r = tu.query_trans_d('000001', '2017-11-12')
# X = r
# Y = pd.DataFrame({'p_change': r['p_change']})
# #
# data = ds.DataSet(X, Y, "日交易记录数据集")
# print(data)
# #
# # print(data.X)
# x = pd.DataFrame()
#
# X = tu.query_trans_d("000001", '2017-11-01')
# Y = pd.DataFrame({'p_change': X['p_change']})
# x1 = X[0:5]
# x2 = X[5:7]
# print('----x1----')
# print(x1)
# print('----x2----')
# print(x2)
# print('----x1 append x2----')
# df = x.append(x1).append(x2)
# print(df)


# dstaset = ds.gen_trans_d_dataset('2017-11-01')
# dstaset.save()

# list = ds.get_all_dataset_filename()
dataset = ds.get_dataset(ds.TO_TRANS_D.get('type'), '过去一年每日交易数据集')
size = len(dataset.X)


index_list = [i for i in range(size)]
print(index_list)
random.shuffle(index_list)
print(index_list)

# train_size = int(size * 0.6)
# valid_size = int(size * 0.2)
# test_size  = int(size * 0.2)
#
# print("train data size %s" % train_size)
# print("valid data size %s" % valid_size)
# print("test  data size %s" % test_size)
#
# Y = dataset.Y.as_matrix()
# print(Y.shape)
#
# train_Y = Y[:train_size]
# valid_Y = Y[train_size:train_size + valid_size]
# test_Y = Y[train_size + valid_size:]
# print('---')
# print(train_Y.shape)
# print(valid_Y.shape)
# print(test_Y.shape)
