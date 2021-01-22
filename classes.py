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

        tryer = []

        for i in range(8, len(lines)-2):
            curr_line = lines[i][:-1] # 去掉回车
            if is_meta(curr_line):
                date_str = curr_line[:19]
                name_str = curr_line[20:]
            elif curr_line is None:
                continue
            else:
                # text
                msg_str = curr_line

            meta = lines[i][:-1]
            msg = lines[i+1][:-1]

            self.msg_list.append(singleMsg(meta, msg))



            # if i%2 == 0: # 偶数: metadata
            #     pass
            #
            # else:   # 奇数: 信息
            #     pass
            #
            #
            # if lines[i].strip("\n") == "[图片]":
            #     lines[i - 2], lines[i - 1], lines[i] = "", "", ""


        print("D")


class singleMsg():
    """单条聊天信息, txt例子:
    > 2020-07-01 12:01:37 wjr 永不平等
    > 就是就是
    """
    def __init__(self, meta:str, msg:str):
        self.date = None
        self.sender = None
        self.msg = msg
        # self.parse_meta()
        is_meta(meta)

    def parse_meta(self):
        """meta:
        """
        pass


def is_meta(line:str):
    """判断是否是包含日期的meta栏:
        2018-07-10 10:32:51 null
        2018-06-15 4:04:50 王珺儒
        2020-06-21 8:39:17 王珺儒 只聊游戏和商品
    """
    re_string = r'^(?P<date>\d{4}-\d{2}-\d{2}\s\d{1,2}:\d{2}:\d{2})\s.*$'
    for string in line:
        if (re.match(re_string, string)):
            print(string, "yes")
        else:
            print(string, "no")

