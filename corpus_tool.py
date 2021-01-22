import os
import shutil
from datetime import datetime
import re

DATA_PATH = "./src"
OUTPUT_PATH = "output"

# def backup_file(file_name):
#     """每次操作复制一份原文件到 BACKUP_PATH文件夹, 添加日期到文件名防止重复
#     >>> backup_file("sample.txt")
#     """
#     if not os.path.exists(BACKUP_PATH):
#         os.makedirs(BACKUP_PATH)
#
#     og_path = os.path.join(DATA_PATH, file_name)
#     split_name = os.path.splitext(file_name)
#     curr_time = datetime.now().strftime(" %m%d-%H%M%S")
#     new_file_name = os.path.join(BACKUP_PATH, split_name[0] + curr_time + split_name[1])
#
#     shutil.copy2(og_path, new_file_name)
#     print("Backup created: " + new_file_name)


def delete_lines_match(file_name: str, match_word: str):
    """删掉完全匹配的一行内容
    >>> delete_lines_match("sample.txt", "d")
    """
    full_path = os.path.join(DATA_PATH, file_name)
    a_file = open(full_path, "r")
    lines = a_file.readlines()
    a_file.close()

    new_file = open(full_path, "w")
    for line in lines:
        if line.strip("\n") != match_word:
            new_file.write(line)

    new_file.close()

def delete_qq_img(file_name: str, match_word: str):
    """删掉qq[图片] 以及发送人的信息
    """
    full_path = os.path.join(DATA_PATH, file_name)
    full_out_path = os.path.join(OUTPUT_PATH, file_name)
    a_file = open(full_path, "r", encoding='UTF-8')
    lines = a_file.readlines()
    a_file.close()

    new_file = open(full_out_path, "w", encoding='UTF-8')

    for i in range(len(lines)):
        if lines[i].strip("\n") == "[图片]":
            lines[i-2], lines[i-1], lines[i]= "", "", ""

    for line in lines:
        new_file.write(line)

    new_file.close()

def delete_qq_img2(file_name: str, match_word: str):
    """测试功能
    """
    full_path = os.path.join(DATA_PATH, file_name)
    full_out_path = os.path.join(OUTPUT_PATH, file_name)
    a_file = open(full_path, "r", encoding='UTF-8')
    lines = a_file.readlines()
    a_file.close()

    # backup_file(file_name)

    new_file = open(full_out_path, "w", encoding='UTF-8')

    re_string = r'^(?:[2-9]\d\d\d)-(?:1[012]|0?[1-9])?-(?:31(?!.(?:0?[2469]|11))|(?:30|29)(?!.0?2)|29(?=.0?2.(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00)))(?:T))|(?:2[0-8]|1\d|0?[1-9])).*'

    re_website = "^((https?|ftp|smtp):\/\/)?(www.)?[a-z0-9]+\.[a-z]+(\/[a-zA-Z0-9#]+\/?).*$"

    for i in range(len(lines)):
        if lines[i] == "\n":
            lines[i] = ""

        elif (re.match(re_string, lines[i])): # 去掉日期
            lines[i] = ""

        elif (re.match(re_website, lines[i])): # 去掉网址
            lines[i] = ""


    for line in lines:
        new_file.write(line)

    new_file.close()

if __name__ == '__main__':
    delete_qq_img2("wjr.txt", "d")
    # backup_file("sample.txt")
