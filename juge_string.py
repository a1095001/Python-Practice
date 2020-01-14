import unicodedata

def is_number(s,i):
    try:
        float(s)                      # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        return True
    except ValueError:                # 如果不能运行float(s)语句，返回False
        pass                          # 
    try:
        for i in s:
            i = unicodedata.numeric(i)
        return True , i
    except (TypeError, ValueError):
        pass
    return False

s = '一'
s , a = is_number(s , 0)
print(s)
print(a)
