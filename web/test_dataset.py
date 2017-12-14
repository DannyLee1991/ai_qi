import dataset as ds
import tudata as tu
import pandas as pd
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

list = ds.get_all_dataset_filename()
print(list)
dataset = ds.get_dataset(list[0])
print(dataset)

# print("X------>")
# print(dstaset['X'])
# print("Y------>")
# print(dstaset['Y'])
