from typing import *
import pyperclip
import pickle
import pandas as pd


SOURCE_DIR = "../bin"
OUTPUT_DIR = "../out"

AVATAR_PICKLE = "../bin/avatar_entries.pickle"




# ====数据相关的操作===


def export_xlsx_vrca(pickle_path:str, filename:str):
    """输出存储的信息到xlsx
    :param pickle_path: "../bin/avatar_entries.pickle" (AVATAR_PICKLE)
    :param filename: xxx.xlsx
    """
    pickle_file = pickle_path
    entry_dict = pickle.load(open(pickle_file, "rb"))
    dict1 = entry_dict
    entry_list = [i for i in entry_dict.values()]

    df = pd.DataFrame(entry_list)

    # df = (df.T)
    print(df)

    df.to_excel(filename)

