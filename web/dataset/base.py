import tudata as tu
import pickle as pk
import os
from config import basedir

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
