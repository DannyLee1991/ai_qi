import dataset as ds
import random
import numpy as np

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
# 将Y 转换成int类别
Y = np.asarray(list(map(int, Y)))
# 变形成 n,1 的形状
Y = Y.reshape(Y.shape[0], 1)
print("Y shape is %s" % Y.shape)

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
