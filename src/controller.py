from models import *
import re
from multiprocessing import Process, Queue


"""
所有handle通用的controller, 基于models
"""

def is_url(s:str) -> bool:
    r = get_URL_from_line(s)
    if not r:
        return False
    return True

def get_URL_from_line(line:str) -> str:
    """
    从一行提取url; 返回输出的url
    """
    if not line:
        return ""
    r = (re.search(re_URL, line))

    if not r:
        return ""
    full_url = f'{r.group(1)}'

    return full_url

def get_space_from_line(line:str):
    return line.find(" ")


def do_subprocess(my_function):
    queue = Queue()
    p = Process(target=my_function, args=(queue, 1))
    p.start()
    p.join() # this blocks until the process terminates
    result = queue.get()
    print (result)