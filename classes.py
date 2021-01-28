import os
import shutil
from datetime import datetime
import re
import csv

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
        with open("test.csv", "w", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            # 先写入columns_name
            writer.writerow(["date", "sender", "message"])

            for i in self.msg_list:
                writer.writerow([i.date, i.sender, i.msg])




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
        self.sender = meta[19:]


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


if __name__ == '__main__':
    parser = msgParser('曜(1127717844).txt')
    parser.to_csv()

    print("Done")
