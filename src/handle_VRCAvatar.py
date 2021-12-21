from typing import *
import pyperclip

sample_text = """---------------------------------------------------------------------------------------------------------------------
Author: ☠☦☣❖
ID: usr_b68fab41-f14b-4176-b968-dafa219f9d3f
Image URL: https://api.vrchat.cloud/api/1/file/file_dcb8cba1-d6fe-4324-9b6e-b2afc6dceaf8/1/file
Avatar id: avtr_3f29809a-812e-4918-8325-b9dbea72ca80
Avatar name: EYO Maid 0․8
Asset url: https://api.vrchat.cloud/api/1/file/file_ba4e6b70-a53b-4de1-90db-ee5ba9a005aa/1/file
Release status: public
Version: 2
standalonewindows
---------------------------------------------------------------------------------------------------------------------"""





def get_avtr_id(raw_str:str):
    """输入notorious信息, 返回avtr_xxx
    """
    start_string = "Avatar id: "
    end_string = "Avatar name:"

    # print(raw_str)

    id_index = raw_str.index(start_string)+len("Avatar id: ")
    id_end = raw_str[id_index:].index(end_string) + id_index
    actual_id = raw_str[id_index: id_end]
    return actual_id

def get_avtr_name(raw_str:str):
    """输入notorious信息, 返回avtr_xxx
    """
    start_string = "Avatar name: "
    end_string = "\n"

    id_index = raw_str.index(start_string)+len("Avatar id: ")
    id_end = raw_str[id_index:].index(end_string) + id_index
    actual_id = raw_str[id_index: id_end]
    return actual_id

def get_release_status(raw_str:str):
    """输入notorious信息, 返回avtr_xxx
    """
    start_string = "Release status: "
    end_string = "\n"

    id_index = raw_str.index(start_string)+len("Avatar id: ")
    id_end = raw_str[id_index:].index(end_string) + id_index
    actual_id = raw_str[id_index: id_end]
    return actual_id



def parse_input(raw_str:str):
    id = get_avtr_id(raw_str)

    pyperclip.copy(id)
    print("已复制: ", id, "\n\n")


def parse_local_command(command:str):
    pass


def parse():

    while(True):
        new_input = input("输入黏贴或指令")

        if (len(new_input) > 20):
            parse_input(new_input)


        else:
            parse_local_command(new_input)


