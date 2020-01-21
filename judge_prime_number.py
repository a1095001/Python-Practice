#使用开根号法进行判别
import unicodedata
import math
import time
import sys

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

def judge(num):
    num = int(num)
    if num == 1:
        return False
    else:
        square_num = math.sqrt(num)
        for i in range(2,square_num + 1):    #创建一个包含2到square_num的'range'
            if (num % i) == 0:
                return False
            else:
                return True
            pass
        pass




num = input('请输入一个质数：')
while is_int(num) == False:
    num = input('非法输入！请重新输入一个合法的整数：')
    temp = num
    num = is_int(num)
    pass
else:
    num = int(num)
    while num < 0:
        key = input('你输入的是一个负数，负数并不是质数！是否将其转换为对应的正数进行判别？  [y/n]')
        if key == 'y':
            num = -num
            num = temp
            judge(num)
            if judge(num) == False:
                print('{}不是一个素数'.format(temp))
                pass
            else:
                print('{}是一个素数'.format(temp))
                pass
            pass
        else:
            print('程序将在1S后结束！')
            time.sleep(1)
            sys.exit(0)
            pass
        pass
    else:
        temp = num
        judge(num)
        if judge(num) == True:
            print('{}是一个素数'.format(temp))
            pass
        else:
            print('{}是一个素数'.format(temp))