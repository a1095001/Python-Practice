'''可切换的摄氏度与华氏度换算器'''

import time
from sys import exit

flag = 0
flag = 'N'
while(flag == 0):
    print('是否要开始换算程序？\n [1]:开始\n [2]:退出')
    mode = input('输入1进入')
    while mode == 1 or mode == 2:
        if mode == 1:
            Celsius = 0
            Fharenheit = 0
            Celsius = float(input('请输入当前温度为：%c℃'%Celsius))
            Fharenheit = (Celsius * 1.8) + 32
            print('{0}℃ 等于{1}℉'.format(Celsius , Fharenheit))
            pass
        elif mode == 2:
            Celsius = 0
            Fharenheit = 0
            Fharenheit = float(input('请输入当前温度为：%F℉'%Fharenheit))
            Celsius = (Fharenheit - 32)/1.8
            print('{2}℉ 等于{3}℃'.format(Fharenheit , Celsius))
            pass
    else flag == 0:
        print('是否要退出换算？y/n?')
        temp = input()
        if temp == 'y':
            print('程序将在1S后退出')
            time.sleep(1)
            exit(0)
            pass
        pass
