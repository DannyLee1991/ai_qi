import tudata as tu
import pickle as pk
import os
from config import basedir
import pandas as pd
from utils.cache import cache

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

    def __str__(self):
        return str(self.info())

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
                "y_label": self.col_y_label()
                }

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

    def save(self):
        path = DATA_SET_PATH
        if not os.path.exists(path):
            os.makedirs(path)

        file = path + os.path.sep + FILE_NAME_FORMAT(self.typeObj['type'], self.name)
        with open(file, 'wb') as f:
            pk.dump(self, f)


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

    def feed(self, code):
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

            self.save_cache(code)

    def save_cache(self, code):
        self.cache_codes.append(code)
