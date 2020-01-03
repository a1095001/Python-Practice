#计算圆的面积

import math
import unicodedata

Pi = math.pi

def calculate():
    r = input('请输入圆的半径：\n')
    while is_number(r) == False or float(r) <= 0:
        print('你输入为非法值，请输入大于0的数！！！\n')
        r = input('请输入半径')
        pass
    else:
        r = float(r)
        area = pow(r , 2)*Pi
        print('圆的面积为：%.3f'%area)
        input('输入回车键退出')
        pass

def is_number(s):
    try:
        float(s)
        return True
        pass
    except ValueError:
        return False
        pass
    try:
        i = 0
        for i in s:
            unicodedata.numeric(i)
            return True
        pass
    except(TypeError, ValueError):
        pass
    return False
calculate()
