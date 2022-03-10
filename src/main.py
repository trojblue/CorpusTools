import argparse
import time, sys, schedule
import handler_VRCAvatar

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
        handler_VRCAvatar.parse(mode="copy")


    elif args.text:

        print("保存到文件, 没实现呢")


    elif args.store:
        print("存储到本地文件")
        handler_VRCAvatar.parse(mode="store")

    elif args.copystore:
        print("存储到本地文件, 并写入剪贴板")
        handler_VRCAvatar.parse(mode="copystore")


    else:
        print("没输入参数, 输入[-h]查看帮助")
        return 0







if __name__ == '__main__':
    do_parse()