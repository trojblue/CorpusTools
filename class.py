class msgParser():
    """工厂设计模式, 用作承担转换工作
    """
    def __init__(self, txt_location:str):
        self.txt_location = txt_location
        self.msg_list = []






class msg():
    """单条聊天信息, txt例子:
    > 2020-07-01 12:01:37 wjr 永不平等
    > 就是就是
    """
    def __init__(self, date, sender, msg:str, qq:str=None):
        self.data = date
        self.sender = sender
        self.msg = msg
        self.qq = qq

