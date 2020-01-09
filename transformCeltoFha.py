'''可切换的摄氏度与华氏度换算器'''

import time
from sys import exit

flag = 0
while(flag == 0):
    print('开始换算程序，请选择模式\n [1]：℃  → ℉\n [2]：℉  → ℃')
    mode = int(input())
    while mode == 1 or mode == 2:
        if mode == 1:
            Celsius = 0
            fahrenheit = 0
            Celsius = float(input('请输入当前温度为：摄氏度'))
            fahrenheit = (Celsius * 1.8) + 32
            print('{0}℃ 等于{1}℉'.format(Celsius , fahrenheit))
            mode = 0
            pass
        elif mode == 2:
            Celsius = 0
            fahrenheit = 0
            fahrenheit = float(input('请输入当前温度为：%F华氏度'%fahrenheit))
            Celsius = (fahrenheit - 32)/1.8
            print('{2}℉ 等于{3}℃'.format(fahrenheit , Celsius))
            mode = 0
            pass
else:
    if flag == 1:
        print('程序将在1S后退出')
        time.sleep(1)
        exit(0)
        pass
    pass
