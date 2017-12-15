from ..base import DATA_SET_PATH, FILE_NAME_FORMAT
import os
import pickle as pk


def get_all_dataset_filename():
    '''
    获取全部的数据集的文件名称
    :return:
    '''
    if os.path.exists(DATA_SET_PATH):
        return os.listdir(DATA_SET_PATH)


def get_all_dataset_info_list():
    '''
    获取所有数据集的info
    :return:
    '''
    infolist = []
    for name in get_all_dataset_filename():
        dataset = _get_dataset(name)
        infolist.append(dataset.info())
    return infolist


def _get_dataset(file_name):
    '''
    根据数据集的文件名称获取数据集对象
    :param file_name:
    :return:
    '''
    filepath = _get_dataset_file_path(file_name)
    with open(filepath, 'rb') as f:
        return pk.load(f)


def get_dataset(type, name):
    '''
    根据数据集的类型和名称 获取数据集
    :param type:
    :param name:
    :return:
    '''
    return _get_dataset(FILE_NAME_FORMAT(type, name))


def _remove_dataset(file_name):
    '''
    移除指定的数据集
    :param file_name:
    :return:
    '''
    path = _get_dataset_file_path(file_name)
    os.remove(path)


def _get_dataset_file_path(file_name):
    '''
    根据数据集文件名 获取数据集路径
    :param file_name:
    :return:
    '''
    return DATA_SET_PATH + os.path.sep + file_name


def remove_dataset(type, name):
    '''
    移除指定类型指定名称的数据集
    :param type:
    :param name:
    :return:
    '''
    _remove_dataset(FILE_NAME_FORMAT(type, name))


def remove_all():
    '''
    删除所有数据集
    :return:
    '''
    for name in get_all_dataset_filename():
        remove_dataset(name)
