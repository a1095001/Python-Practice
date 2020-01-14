import unicodedata

def is_number(s):
    try:
        float(s)                      # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        return True
    except ValueError:                # 如果不能运行float(s)语句，返回False
        pass                          # 
    try:
        for i in s:
            unicodedata.numeric(s)
            return True
    except (TypeError, ValueError):
        pass
    return False