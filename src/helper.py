import os

import pyperclip
from typing import *
from models import *


def to_clipboard(s:str):
    """复制s到剪贴板"""
    pyperclip.copy(s)


def save_file(str_list: List[str], path: str):
    """
    :param file: list of lines
    :param path: relative path (of OUTPUT_DIR) to be saved
    :return:
    """
    full_save_path = os.path.join(OUTPUT_DIR, path)
    f = open(full_save_path, "w")
    for element in str_list:
        f.write(element + "\n")
    f.close()


