import dataset as ds
import random
import numpy as np
from web.dataset_preproces.common import uniform_distribution

info_list = ds.get_all_dataset_info_list()
print(info_list)

dataset_name = info_list[0]['name']

dataset = ds.get_dataset(ds.TO_TRANS_D.get('type'), dataset_name)
size = dataset.datasize()

# 创建数据索引
index_list = [i for i in range(size)]
# 数据索引打乱
random.shuffle(index_list)

train_size = int(size * 0.6)
valid_size = int(size * 0.2)
test_size = int(size * 0.2)

X = dataset.X.as_matrix()
Y = dataset.Y.as_matrix()

# 剔除日期字段
X = X[:, 1:]
# 改变数据的dtype
X = X.astype('float')


# 将Y 转换成int类别
# 由于tensorflow 接受的类别标签必须是 大于0的数 所以对Y值转成int之后再 +10
# Y = np.asarray(list(map(lambda x: int(x) + 10, Y)))
Y = np.asarray(list(map(float, Y)))

# def label_func(num):
#     # 设置数据分段区间，使得各个区间保持均匀分布
#     split_points = [-10.08, -2.3900000000000001, -1.4199999999999999, -0.84999999999999998, -0.40999999999999998, 0.0, 0.28999999999999998, 0.68999999999999995, 1.24, 2.25, 10.16]
#     for index, point in enumerate(split_points):
#         if num < point:
#             return index
#     return len(split_points)
#
# Y = np.asarray(list(map(label_func, Y)))

Y = uniform_distribution(Y,21,'n')
print(Y)

print("Y shape is %s" % str(Y.shape))

# 生成训练集
train_X = X[index_list[:train_size]]
train_Y = Y[index_list[:train_size]]

# 生成验证集
valid_X = X[index_list[train_size:train_size + valid_size]]
valid_Y = Y[index_list[train_size:train_size + valid_size]]

# 生成测试集
test_X = X[index_list[train_size + valid_size:]]
test_Y = Y[index_list[train_size + valid_size:]]

print("orig X shape %s" % (str(X.shape)))
print("orig Y shape %s" % (str(Y.shape)))

print("train X shape %s" % (str(train_X.shape)))
print("train Y shape %s" % (str(train_Y.shape)))
print("valid X shape %s" % (str(valid_X.shape)))
print("valid Y shape %s" % (str(valid_Y.shape)))
print("test X shape %s" % (str(test_X.shape)))
print("test Y shape %s" % (str(test_Y.shape)))

print(test_Y)

print(test_X.dtype)

uniqueTrain = set()
for l in train_Y:
    uniqueTrain.add(l)

uniqueTrain = list(uniqueTrain)
numClasses = len(uniqueTrain)
print(uniqueTrain)
print(numClasses)

#
#
#
#
#
# 画图逻辑
# import matplotlib.pyplot as plt
#
# fig, axs = plt.subplots()
#
# axs.hist(Y, bins=numClasses)
#
# plt.show()
