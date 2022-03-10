from typing import *
import pyperclip
import pickle

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

ENTRY_DICT = {}
try:
    pickle_file = "../bin/avatar_entries.pickle"
    ENTRY_DICT = pickle.load(open(pickle_file, "rb"))
except Exception:
    yn = input("load出错, 是否创建新文件? (y/n)")
    if (yn == "y" or yn == "Y"):
        pass # 覆写文件
    else:
        exit(1)

CATEGORY = "default"
print("已加载", len(ENTRY_DICT.keys()), "条记录")


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


def enumerate_dict(raw_str:str):
    """生成单个dict"""
    my_dict = dict()
    curr_name = raw_str.index("Author: ")
    curr_usr_id = raw_str.index("ID: ")
    curr_img_url = raw_str.index("Image URL: ")
    curr_avatar_id = raw_str.index("Avatar id: ")
    curr_avatar_name = raw_str.index("Avatar name: ")
    curr_asset_url = raw_str.index("Asset url: ")
    curr_status = raw_str.index("Release status: ")
    curr_version = raw_str.index("Version: ")

    my_dict["avatar_name"] = raw_str[curr_avatar_name + len("Avatar name: "): curr_asset_url]
    my_dict["avatar_id"] = raw_str[curr_avatar_id+ len("Avatar id: "):curr_avatar_name]
    my_dict["category"] = CATEGORY


    my_dict["name"] = raw_str[curr_name + len("Author: "):curr_usr_id]
    my_dict["user_id"] = raw_str[curr_usr_id + len("ID: "):curr_img_url]
    my_dict["img_url"] = raw_str[curr_img_url+ len("Image URL: "):curr_avatar_id]
    my_dict["asset_url"] = raw_str[curr_asset_url+ len("Asset url: "):curr_status]
    my_dict["status"] = raw_str[curr_status+ len("Release status: "):curr_version]


    version_str_raw = raw_str[curr_version+ len("Version: "):]
    my_dict["version"] = version_str_raw[: version_str_raw.index("------")]
    return my_dict

def store_info(raw_str:str):
    """
    需要事先存在avatar_entries.pickle, 没写exception
    my_dict: 格式见enumerate_dict()
    """
    my_dict = enumerate_dict(raw_str)

    # TODO: 更新信息功能
    if (my_dict["avatar_id"]) in ENTRY_DICT:
        print("记录已经存在")
        return

    ENTRY_DICT[my_dict["avatar_id"]] = my_dict
    pickle.dump(ENTRY_DICT, open(pickle_file, "wb"))
    print("[%s] 写入成功" %CATEGORY)
    return my_dict



def parse(mode:str):
# 从main转到vrcAvatar
    global CATEGORY
    category_prompt = input("输入类别名称: waifu, erp, creature, small, funny, [default]")
    if category_prompt:
        CATEGORY = category_prompt

    if (mode == "copy"):
        while(True):
            new_input = input("黏贴内容: ")

            if (len(new_input) > 20):
                id = get_avtr_id(new_input)
                pyperclip.copy(id)
                print("已复制: ", id, "\n\n")

    elif (mode == "store"):
        while (True):
            new_input = input("黏贴内容: ")

            if (len(new_input) > 20):
                store_info(new_input)

    elif (mode == "copystore"):
        while (True):
            new_input = input("黏贴内容: ")

            if (len(new_input) > 20):
                curr_dict = store_info(new_input)
                curr_id = curr_dict["avatar_id"]
                pyperclip.copy(curr_id)
                print("已复制: ", curr_id, "\n\n")


