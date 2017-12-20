import numpy as np
import math


def uniform_distribution(Y, n, l_type='b'):
    '''
    平均分布

    将Y按照值的大小进行均匀分布的方式分割成n等分
    并生成对应的类别标签

    :param Y: 数据源  形状为(num,)
    :param n: 将数据分割为n等分
    :param l_type: 分割数据之后 标签的取值类别{'b','s','n'}
                'b' : 类别标签为区间范围内的最大值
                's' : 类别标签为区间范围内的最小值
                'n' : 类别标签为区间范围内的平均值

    :return:

    eg：
    Y = [1,1,2,3,4,4,5,6,7]
    n = 5
    l_type = 'b'
    result = [1 1 3 3 4 4 6 6 7]

    n = 3
    l_type = 's'
    result = [1 1 1 2 2 2 4 4 4]

    n = 5
    l_type = 'n'
    result = [ 1.   1.   2.   2.   3.5  3.5  5.   5.   6.5]

    '''

    node_list = gen_nodelist(Y, n)
    toY = []
    for num in Y:
        index, val = get_label(num, node_list, l_type)
        toY.append(index)

    print("node list >>")
    print(node_list)
    return np.array(toY)


def get_label(num, node_list, l_type):
    # 下限
    lm = 0
    # 上限
    um = 0
    target = 0

    # 节点区间是(lm,um]
    for index, node in enumerate(node_list):
        if node >= num:
            if index > 0:
                um = node
                lm = node_list[index - 1]
                target = index
                break

    label = ''
    if l_type == 's':
        label = lm
    elif l_type == 'b':
        label = um
    elif l_type == 'n':
        label = (lm + um) / 2

    return target, label


def gen_nodelist(data, n):
    '''
    生成节点列表  节点是指示数据的分割点
    :param data: 原始数据 需要被分割的数据
    :param n: 分割的份数
    :return:
    '''
    sorted_list = sorted(data)
    size = len(sorted_list)
    node_list = []
    block_size = math.ceil(size / n)
    for index, item in enumerate(sorted_list):
        if (index + 1) % block_size == 0:
            node_list.append(item)
        elif index == 0:
            node_list.append(item)
        elif index == size - 1:
            node_list.append(item)

    return node_list

#
#
#
#
# Y = np.array([1,1,2,3,4,4,5,6,7])
# print("orig y:")
# print(Y)
# print("orig y shape:")
# print(Y.shape)
# result = uniform_distribution(Y, 5, 'n')
#
# print(result)
#
