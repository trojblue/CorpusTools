import os
import shutil
from datetime import datetime
import re

DATA_PATH = "./src"
OUTPUT_PATH = "output"

class msgParser():
    """工厂设计模式, 用作承担转换工作
    """
    def __init__(self, filename:str):
        """sender: 与之对话的人
        """
        self.filename = filename
        self.msg_list = []
        self.sender = ""
        self.parse()

    def parse(self):
        """把输入地址转成list
        """
        full_path = os.path.join(DATA_PATH, self.filename)
        full_out_path = os.path.join(OUTPUT_PATH, self.filename)

        a_file = open(full_path, "r", encoding='UTF-8')
        lines = a_file.readlines()
        a_file.close()

        self.sender = lines[5]

        self.add_messages(lines)

    def add_messages(self, lines):
        """读取lines, 添加single messages object到self
        """
        meta_line = None
        for i in range(8, len(lines) - 2):

            curr_line = lines[i][:-1]  # 去掉回车

            if is_meta(curr_line):
                # 处理前面的meta_line

                if meta_line is not None:
                    prev_meta = lines[meta_line][:-1]
                    prev_msgs = lines[meta_line + 1: i]
                    prev_candidates = " ".join(prev_msgs).replace("\n", ' ').strip(' ')
                    self.msg_list.append(singleMsg(prev_meta, prev_candidates))

                meta_line = i

    def to_csv(self):
        """输出为csv"""
        pass



class singleMsg():
    """单条聊天信息, txt例子:
    > 2020-07-01 12:01:37 wjr 永不平等
    > 就是就是
    """

    def __init__(self, meta: str, msg: str):
        self.date = None
        self.sender = None
        self.msg = msg
        self.parse_meta(meta)

    def __repr__(self):
        return (show_time(self.date) + "    |    <" + self.sender + ">   " + self.msg)

    def parse_meta(self, meta):
        """meta: single line meta
        """
        date_time_obj = parse_time(meta[:19])
        self.date = date_time_obj
        self.sender = meta[20:]


def is_meta(line: str):
    """判断是否是包含日期的meta栏:
        2018-07-10 10:32:51 null
        2018-06-15 4:04:50 王珺儒
        2020-06-21 8:39:17 王珺儒 只聊游戏和商品
    """
    re_string = r'^(?P<date>\d{4}-\d{2}-\d{2}\s\d{1,2}:\d{2}:\d{2})\s.*$'
    if (re.match(re_string, line)):
        return True
    else:
        return False


def parse_time(date_string: str):
    return datetime.strptime(date_string.strip(' '), '%Y-%m-%d %H:%M:%S')


def show_time(date_obj):
    return date_obj.strftime('%Y-%m-%d %H:%M:%S')

import argparse
import time, sys, schedule
import handle_vrchat

def do_parse():
    """
    命令行读取参数
    """
    parser = argparse.ArgumentParser()
    action_group = parser.add_mutually_exclusive_group()
    action_group.add_argument("-c", "--copy", help="复制到剪贴板", action="store_true")
    action_group.add_argument("-t", "--text", help="写入到txt文件", action="store_true")
    action_group.add_argument("-s", "--store", help="保存到内部数据库", action="store_true")
    action_group.add_argument("-cs", "--copystore", help="保存到数据库, 并黏贴剪贴板", action="store_true")

    decode_mode = parser.add_mutually_exclusive_group()
    decode_mode.add_argument("--vrca", help="vrchat avatar模式", action="store_true")

    args = parser.parse_args()


    if args.copy:

        print("实时复制到剪贴板")
        handle_vrchat.parse_command(mode="copy")


    elif args.text:

        print("保存到文件, 没实现呢")


    elif args.store:
        print("存储到本地文件")
        handle_vrchat.parse_command(mode="store")

    elif args.copystore:
        print("存储到本地文件, 并写入剪贴板")
        handle_vrchat.parse_command(mode="copystore")


    else:
        print("没输入参数, 输入[-h]查看帮助")
        return 0




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


def simplify_sender(file_name: str, match_word: str):
    """删掉发送人信息, 保留[图片] tag
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
    delete_qq_img2("thoughts.txt", "d")
    # backup_file("sample.txt")



if __name__ == '__main__':
    do_parse()