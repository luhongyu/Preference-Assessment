# coding=utf-8
import pandas as pd
class PDtable:
    """
    .add(data, "colname")
    .to_pandas
    """
    def __init__(self):
        self.column_datas = {}
        self.column_names = []

    def add(self, data, colname):
        if colname not in self.column_datas:
            self.column_datas[colname] = []
            self.column_names.append(colname)

        self.column_datas[colname].append(data)

    def to_pandas(self):
        return pd.DataFrame(self.column_datas)[self.column_names]

