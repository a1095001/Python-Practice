'''可切换的摄氏度与华氏度换算器'''
while 1:
    Celsius = float(input('请输入当前温度为'))
    Fharenheit = (Celsius * 1.8) + 32
    print('{0}摄氏度等于{1}华氏度'.format(Celsius , Fharenheit))