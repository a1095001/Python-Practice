import unicodedata

def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
    try:
        for i in num:
            unicodedata.numeric(i)
            return True
    except (TypeError,ValueError):
        pass
    return False

num = input('请输入一个质数')
while True:
    if is_int(num) == False:
        print('非法输入，请重新输入一个合法的整数：')