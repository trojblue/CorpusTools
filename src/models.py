import os
from typing import *
import pyperclip
import pickle
import pandas as pd


SOURCE_DIR = "../bin"
OUTPUT_DIR = "../out"

AVATAR_PICKLE = "../bin/avatar_entries.pickle"




# ====数据相关的操作===

def export_clipboard(s:str):
    """复制string s到剪贴板
    :param s: 要复制的string
    """
    pyperclip.copy(s)


def export_vrca_xlsx(pickle_path:str, filename:str):
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


def export_lines_txt(str_list: List[str], path: str):
    """
    :param str_list: List[string]
    :param path: relative path (of OUTPUT_DIR)
    """
    full_save_path = os.path.join(OUTPUT_DIR, path)
    f = open(full_save_path, "w")
    for element in str_list:
        f.write(element + "\n")
    f.close()
