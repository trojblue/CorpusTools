import re
from handle_qq import *

def try_list():
    lst = ["one", "two", "three"]
    lst.remove(1)
    print(lst)

def try_regex():
    """
    2018-07-10 10:32:51 null
    2018-06-15 4:04:50 王珺儒
    2020-06-21 8:39:17 王珺儒 只聊游戏和商品
    """
    #(?P<year>^\d{4} )-(?P<month>\d{2})-(?P<day>\d{2} )
    test_strings = ["2018-07-10 10:32:51 null", '2018-06-15 4:04:50 王珺儒',
                   "2020-06-21 8:39:17 王珺儒 只聊游戏和商品", "2020-05-21 5:34:55 現實逃避p(1908687236)",
                   "2020-05-21 5:35:45 Βασιλιάς<katiaykjln@hotmail.com>", "2020-06-26 9:00:54 提醒基德小助手(2487878871)"]
    # re_string = r'^(?:[2-9]\d\d\d)-(?:1[012]|0?[1-9])?-(?:31(?' \
    #             '!.(?:0?[2469]|11))|(?:30|29)(?!.0?2)|29(?=' \
    #             '.0?2.(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468]' \
    #             '[048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26]' \
    #             ')00)))(?:T))|(?:2[0-8]|1\d|0?[1-9])).*'

    # r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})\s(?P<hour>\d{1,2}):(?Pd\d{2}:\d{2}\s.*$'
    re_string = r'^(?P<date>\d{4}-\d{2}-\d{2}\s\d{1,2}:\d{2}:\d{2})\s.*$'
    for string in test_strings:
        if (re.match(re_string, string)):
            print(string, "yes")
        else:
            print(string, "no")


def try_datetime():
    import datetime

    date_time_str = '2018-06-29 08:15:27'
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

    def show_time(date_obj):
        return date_obj.strftime('%Y-%m-%d %H:%M:%S')

    s = show_time(date_time_obj)

    print('Date:', date_time_obj.date())
    print('Time:', date_time_obj.time())
    print('Date-time:', date_time_obj)


def try_msgParse():
    file_name = "wjr.txt"
    parser = msgParser(file_name)

    print("D")




if __name__ == '__main__':
    # print(8%2, 9%2)
    # try_datetime()
    try_msgParse()
    # try_regex()
