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

'''
#  方法二：递归实现
def factorial(number):
    if number < 1:
        return False
    elif number == 1:
        return 1
    else:
        return number * factorial(number - 1)

num = int(input('请输入您要计算的数：'))
print('{}! = {}'.format(num , factorial(num)))
'''

#  方法三：循环语句
num = int(input('请输入要计算的数字：'))
factorial = 1
while num < 0:
    num = input('负数没有阶乘！请重新输入一个自然数：')
    pass
if num == 1 or 0:
    print('1! = 1')
    pass
elif num > 1:
    for count in range(1 , num + 1 , 1):
        factorial = factorial * count
        pass
    print('{0}! = {1}'.format(count , factorial))

# 还可以使用reduce()函数来实现