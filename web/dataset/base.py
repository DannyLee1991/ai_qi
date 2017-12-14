import tudata as tu
import pickle as pk
import os

DATA_SET_PATH = './_dataset'

class DataSet():
    def __init__(self, X, Y, name, des=''):
        self.X = X
        self.Y = Y
        self.name = name
        self.des = des
        self.info = self._info()

    def __str__(self):
        return str(self.des)

    def _info(self):
        return {"name": self.name,
                "des": self.des,
                "size": len(self.X),
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

        file = path + os.path.sep + self.name + ".pkl"
        with open(file,'wb') as f:
            pk.dump(self,f)
