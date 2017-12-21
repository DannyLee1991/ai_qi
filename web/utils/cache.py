# coding=utf-8
import pickle, os, hashlib
from config import basedir

CACHE_PATH = basedir + '/_cache'

mem_cache = {}


# 写入文件缓存
def write_file_cache(cache_name, cache):
    with open(cache_name, 'wb') as f:
        pickle.dump(cache, f, True)


# 写入内存缓存
def write_mem_cache(cache_name, cache):
    mem_cache[cache_name] = cache


# 计算md5
def md5(arg):
    md5 = hashlib.md5()
    md5.update(str(arg).encode("utf8"))
    return md5.hexdigest()


def cache(use_mem=False, use_file=True, print_log=False, cache_path=CACHE_PATH):
    # use_mem = True
    # use_file = True
    # print_log = True

    '''
    缓存装饰器
    在返回参数需要被缓存的方法上添加此装饰器，即可为方法添加文件缓存。例如：
    @cache()
    def func():
        return obj
    :return:
    '''

    def _cache(func):
        cache_file = cache_path + os.path.sep + func.__name__

        def wrapper(*args, **kwargs):
            args_str = ""

            if args:
                args_str += "_args:"
                for arg in args:
                    args_str += "|" + md5(arg)

            if kwargs:
                args_str += "_kwargs:"
                for k in kwargs.keys():
                    args_str += "(" + k + "-" + md5(kwargs.get(k)) + ")"

            args_str = md5(args_str)

            # 带有参数的缓存文件名称
            cache_file_with_args = cache_file + args_str
            # 使用内存缓存
            if use_mem:
                if cache_file_with_args in mem_cache.keys():
                    if print_log:
                        print("load from mem cache -> %s" % cache_file_with_args)
                    return mem_cache[cache_file_with_args]

            # 使用文件缓存
            if use_file:
                try:
                    if os.path.exists(cache_file_with_args):
                        with open(cache_file_with_args, 'rb') as f:
                            cache = pickle.load(f)
                            if cache is not None:
                                if print_log:
                                    print("load from file cache -> %s" % cache_file_with_args)
                                if use_mem:
                                    write_mem_cache(cache_file_with_args, cache)
                                return cache
                except Exception as e:
                    if print_log:
                        print(e)
                    pass
            if not os.path.exists(cache_path):
                os.makedirs(cache_path)
            result = func() if len(args) == len(kwargs) == 0 else func(*args, **kwargs)
            # 写入文件缓存
            if use_file:
                write_file_cache(cache_file_with_args, result)
            # 写入内存缓存
            if use_mem:
                write_mem_cache(cache_file_with_args, result)
            if print_log:
                print("load from function -> %s" % cache_file_with_args)
            return result

        return wrapper

    return _cache
