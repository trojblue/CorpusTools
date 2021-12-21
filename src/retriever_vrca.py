from typing import *
import pyperclip
import pickle

pickle_file = "../bin/avatar_entries.pickle"
ENTRY_DICT = pickle.load(open(pickle_file, "rb"))
print("已加载", len(ENTRY_DICT.keys()), "条记录")


import pandas as pd



def export_xlsx():
    """输出存储的信息到xlsx
    """
    dict1 = ENTRY_DICT

    df = pd.DataFrame(data=dict1, index=[0])

    df = (df.T)

    print(df)

    df.to_excel('dict1.xlsx')


if __name__ == '__main__':
    export_xlsx()