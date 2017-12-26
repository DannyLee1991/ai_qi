import tudata as tu
import pickle as pk
import os
from config import basedir
import pandas as pd
import random

DATA_SET_PATH = basedir + '/_dataset'

type_func = lambda type, name: {"type": type, "name": name}

TO_TRANS_D = type_func("trans_d", "每日交易数据")

DATASET_TYPE_OBJ_LIST = [
    TO_TRANS_D,
]

FILE_NAME_FORMAT = lambda type, name: "%s--%s.pkl" % (type, name)


def get_all_types():
    '''
    获取所有的类型
    :return:
    '''
    types = []
    for t in DATASET_TYPE_OBJ_LIST:
        type = t['type']
        types.append(type)
    return types


class DataSet():
    def __init__(self, typeObj, name, X, Y, des):
        self.X = X
        self.Y = Y
        self.typeObj = typeObj
        self.name = name
        self.des = des
        # 数据集是否完成创建（只有完整的数据集才可以被送入预处理阶段）
        self.isOK = False

    def __str__(self):
        return str(self.info())

    def set_isOK(self, isOk):
        self.isOK = isOk

    def datasize(self):
        return len(self.X)

    def info(self):
        return {"name": self.name,
                "typeObj": self.typeObj,
                "des": self.des,
                "datasize": self.datasize(),
                "x_shape": self.X.shape,
                "y_shape": self.Y.shape,
                "x_col": self.col_x(),
                "y_col": self.col_y(),
                "x_label": self.col_x_label(),
                "y_label": self.col_y_label(),
                "isOK": self.isOK
                }

    def random_pick(self):
        size = self.datasize()
        index = random.randint(0, size - 1)
        return self.get_row(index)

    def get_row(self, index):
        x = self.X.iloc[index]
        y = self.Y.iloc[index]
        return {'x': x, 'y': y}

    def _col(self, which):
        return [column for column in which]

    def _col_label(self, which):
        labels = []
        for c_n in self._col(which):
            # 如果在标签字典中找到  则添加标签，否则以当前列名作为标签名
            if c_n in tu.COLUMN_LABEL_DICT.keys():
                label = tu.COLUMN_LABEL_DICT[c_n]
                labels.append(label)
            else:
                labels.append(c_n)
        return labels

    def col_x(self):
        return self._col(self.X)

    def col_x_label(self):
        return self._col_label(self.X)

    def col_y(self):
        return self._col(self.Y)

    def col_y_label(self):
        return self._col_label(self.Y)

    def get_label_name(self, which):
        '''
        获取标签的名称
        :param which:
        :return:
        '''
        label_name_list = []
        label_name_list.extend(self.col_x_label())
        label_name_list.extend(self.col_y_label())
        label_list = []
        label_list.extend(self.col_x())
        label_list.extend(self.col_y())
        index = label_list.index(which)
        return label_name_list[index]

    def save(self):
        path = DATA_SET_PATH
        if not os.path.exists(path):
            os.makedirs(path)

        file = self._file_path()
        with open(file, 'wb') as f:
            pk.dump(self, f)

    def _file_name(self):
        return FILE_NAME_FORMAT(self.typeObj['type'], self.name)

    def _file_path(self):
        return DATA_SET_PATH + os.path.sep + self._file_name()

    def file_size(self):
        '''
        获取数据集文件大小
        :return:
        '''
        file = self._file_path()
        fsize = os.path.getsize(file)
        fsize = fsize / float(1024 * 1024)
        return round(fsize, 2)

    def dump_info(self):
        self.min_info = {"X": self.X.min(), "Y": self.Y.min()}
        self.max_info = {"X": self.X.max(), "Y": self.Y.max()}
        self.median_info = {"X": self.X.median(), "Y": self.Y.median()}
        self.var_info = {"X": self.X.var(), "Y": self.Y.var()}
        self.std_info = {"X": self.X.std(), "Y": self.Y.std()}
        self.skew_info = {"X": self.X.skew(), "Y": self.Y.skew()}
        self.kurt_info = {"X": self.X.kurt(), "Y": self.Y.kurt()}

    def complete(self):
        '''
        完成创建
        :return:
        '''
        self.set_isOK(True)
        self.dump_info()
        self.save()


class TransDDataSet(DataSet):
    '''
    日交易数据集
    '''

    def __init__(self, typeObj, name, X, Y, des, start_date, end_date, offset_day):
        '''
        :param typeObj:
        :param name:
        :param X:
        :param Y:
        :param des:
        :param start_date: 数据起始日期
        :param end_date: 数据结束日期
        :param offset_day: Y标签数据 相对X标签日期的偏移天数
        '''
        super(TransDDataSet, self).__init__(typeObj, name, X, Y, des)
        self.start_date = start_date
        self.end_date = end_date
        self.offset_day = offset_day
        self.cache_codes = []

    def info(self):
        info = super(TransDDataSet, self).info()
        info['start_date'] = self.start_date
        info['end_date'] = self.end_date
        info['offset_day'] = self.offset_day
        return info

    def feed_item(self, code):
        if self.isOK:
            print("数据集以完整获取")
            return

        if code in self.cache_codes:
            print("code = %s 数据已存在，不需要重复获取" % code)
        else:
            df = tu.query_trans_d(code, self.start_date, self.end_date)
            # 由于涨跌幅是次日的  所以要对数据进行'错位' 并且'错位之后'对X剔除末尾行，对Y剔除首行
            x = df[:-self.offset_day]
            y = pd.DataFrame({'p_change': df['p_change']})[self.offset_day:]
            if len(self.X) > 0:
                self.X = self.X.append(x, ignore_index=True)
            else:
                self.X = x
            if len(self.Y) > 0:
                self.Y = self.Y.append(y, ignore_index=True)
            else:
                self.Y = y

            # 记录本次获取到的缓存位
            self.cache_codes.append(code)

            self.save()

    def feed_all(self):
        if self.isOK:
            print("数据集以完整获取")
            return

        for index, code in enumerate(tu.all_trans_d_code()):
            self.feed_item(code)
            print("---【%s】执行一次保存操作 x shape %s---" % (self.name, self.X.shape))

        # 数据集创建完成
        self.complete()
        print('%s 数据集创建成功' % self.name)
