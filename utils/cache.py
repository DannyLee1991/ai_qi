import pickle as pk
import os

CACHE_FILE_PATH = '../_cache'


def check_cache_path_exist():
    '''
    检查缓存目录是否存在
    :return:
    '''
    if not os.path.exists(CACHE_FILE_PATH):
        os.mkdir(CACHE_FILE_PATH)

def write_cache(file_name, obj):
    '''
    写入缓存
    :param file_name:
    :param obj:
    :return:
    '''
    check_cache_path_exist()
    file_path = CACHE_FILE_PATH + "/" + file_name
    with open(file_path, 'wb') as f:
        pk.dump(obj,f)

def read_cache(file_name):
    check_cache_path_exist()
    file_path = CACHE_FILE_PATH + "/" + file_name
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            return pk.load(f)

