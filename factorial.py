#  计算阶乘
import math
import unicodedata
'''
#  方法一：直接调用math模块的阶乘函数

num = int(input("请输入一个数字："))
if num < 0:
    print("负数没有阶乘！")
    pass
else:
    print("{}! = {}".format(num , math.factorial(num)))
'''

#  方法二：递归实现
def factorial(number):
    if number > 1:
        return number * factorial(number - 1)

num = int(input('请输入您要计算的数：'))
