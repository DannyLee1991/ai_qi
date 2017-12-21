import dataset as ds
import random
import numpy as np
from web.dataset_preproces.common import uniform_distribution
from utils.cache import cache

dataset_name = "过去一年每日交易数据集"


@cache(use_file=True)
def pp_trans_d_for_model(name):
    dataset = ds.get_dataset(ds.TO_TRANS_D.get('type'), name)
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

    Y = uniform_distribution(Y, 21, 'n')

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

    return {"train_X": train_X,
            "train_Y": train_Y,
            "valid_X": valid_X,
            "valid_Y": valid_Y,
            "test_X": test_X,
            "test_Y": test_Y}


pp_trans_d_for_model(dataset_name)
