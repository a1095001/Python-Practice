import sys
import math
import time
import unicodedata

def is_int(flag):
    try:
        int(flag)
        return True
    except ValueError:
        pass
    try:
        unicodedata.numeric(flag)
        return True
    except(TypeError , ValueError):
        pass
    return False

bouldery = input('请输入素数表范围：')
flag = is_int(bouldery)
i = 0
while flag == False:
    bouldery = input('你输入的不是整数！请重新输入一个正整数：')
    flag = is_int(bouldery)
    pass
else:
    bouldery = int(bouldery)
    while bouldery <= 1:
        bouldery = int(input('你输入的是一个负数！请重新输入一个正整数：'))
        i = i + 1
        if i == 3:
            print('你已经连续三次输入错误，程序将在1S后关闭！！！')
            time.sleep(1)
            sys.exit(0)
            pass
        pass