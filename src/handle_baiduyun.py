from typing import *
from controller import *
import webbrowser
sample_text = """链接： https://pan.baidu.com/s/1LQbrPC5LMG_0h3wt2k0WHg   提取码：tk20 == == 客官您好！ 订单2512189764920274961给您上菜啦： 链接： https://pan.baidu.com/s/1evb3BhKgncfm4wGWYsTm6g   提取码：1234 满意再来光临哈！ == == 下面发的内容是你购买的订单号： 2512189764920274961 的全部内容哦~ 链接： https://pan.baidu.com/s/1no4uSOxmkvTZ-Ps3M64J7Q   提取码：ayc0 祝你每天都有好心情哦~ =="""


def append_links(curr_list:List, url:str, pswd:str):
    """链接和密码, 添加到list
    :param curr_list: List[Dict{'url':str, 'pswd':str}]
    """
    my_dictionary = {'url' : url, 'pswd' : pswd}
    curr_list.append(my_dictionary)



def parse_text(text:str)-> List[Dict]:
    """
    :param text: 不带空格的所有百度云内容 (sample_text)
    :return: 提取的链接
    """
    split_text = text.split(' ')
    url_list = []
    curr_url = ""

    for line in split_text:
        url = get_URL_from_line(line)
        if (url != ""):
            curr_url =  url

        if ("提取码：") in line:
            curr_pswd = line.split("提取码：")[1]
            # has_pswd = True
            append_links(url_list, curr_url, curr_pswd)

    return url_list



def open_link_all(url_list:List[Dict]):
    """浏览器自动打开链接, 并复制密码
    """
    print("len(url_list) = %s" %(len(url_list)))
    for i in range (len(url_list)):
        curr_url, curr_pswd = url_list[i]['url'], url_list[i]['pswd']
        short_url = curr_url.split("https://pan.baidu.com")[1]
        webbrowser.open(curr_url, new=2)
        export_clipboard(curr_pswd)
        input("第%s个, %s: %s  回车以进行下一个"%(i+1, short_url, curr_pswd))

    print("DONE")



if __name__ == '__main__':
    # parse_text(sample_text)
    input_text = input("使用方法: 用ditto全部复制一遍, 一起黏贴, 用特殊黏贴去掉换行符\n")
    url_list = parse_text(input_text)
    open_link_all(url_list)
