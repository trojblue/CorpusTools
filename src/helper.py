import pyperclip



def to_clipboard(s:str):
    """复制s到剪贴板"""
    pyperclip.copy(s)

