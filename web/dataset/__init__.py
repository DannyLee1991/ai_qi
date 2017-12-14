from .base import *
from .gen_dataset.common_dataset import *
from .get_dataset import *

type_func = lambda type, name, func: {"type": type, "name": name, "func": func}

TYPE_TRANS_D = "trans_d"

DATASET_CREATER_LIST = [
    type_func(TYPE_TRANS_D, "每日交易数据", gen_trans_d_dataset),
]


def get_all_types():
    '''
    获取所有的类型
    :return:
    '''
    types = []
    for t in DATASET_CREATER_LIST:
        type = t['type']
        types.append(type)
    return types
