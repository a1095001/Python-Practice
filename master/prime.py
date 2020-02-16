# Python 程序用于检测用户输入的数字是质数还是合数
import sys
import math
import time

# 质数大于 1
def judge_prime(num):
    num = int(num)
    if num == 1:
        return False
    else:
        square_num = math.floor(num ** 0.5)
        for s in range(2,(square_num + 1)):    #创建一个包含2到square_num的'range'，查找因子
            if (num % s) == 0:
                return False
        else:
            return True

# 用户输入数字
#num = int(input("请输入一个数字: "))
bouldery = int(input('请输入一个判断范围：'))
prime_list = []
flag = False
temp = 0
for i in range(2 , bouldery , 1):
    temp = i
    flag = judge_prime(i)
    while flag == True:
        prime_list.append(temp)                #.append()  每次只能添加一个元素
        flag = False
        print(prime_list)
        pass
    else:
        pass