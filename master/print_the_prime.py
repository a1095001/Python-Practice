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

def judge_prime(num):
    num = float(num)
    if num == 1:
        return False
    else:
        square_num = math.floor(num ** 0.5)
        for n in range(2,square_num + 1):    #创建一个包含2到square_num的'range'，查找因子
            if (num % n) == 0:
                return False
            else:
                return True
            pass
        pass

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
        i += 1
        if i == 3:
            print('你已经连续三次输入错误，程序将在1S后关闭！！！')
            time.sleep(1)
            sys.exit(0)
            pass
        pass
    else:
        s = 0
        temp = 0
        prime_number = []
        for s in range(1 , bouldery , 1):
            temp = s
            list_flag = judge_prime(s)
            while list_flag == True:
                prime_number.append(temp)
                list_flag = False
                pass
            else:
                pass
            pass
        print(prime_number)
