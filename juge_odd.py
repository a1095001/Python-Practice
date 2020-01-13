import unicodedata

def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        pass
    try:
        unicodedata.numeric(number)        
        return True
    except (TypeError, ValueError):
        pass
    return False

number = input('请输入一个整数：')
while is_int(number) == False:
    print('非法输入！请重新输入一个合法整数！')
    number = input('请输入合法整数：')
    is_int(number)
    pass
else:
    int(number)
    temp = number % 2
    if temp != 0:
        print('{}是一个奇数'.format(number))
        pass
    else:
        print('{}是一个偶数'.format(number))
        pass