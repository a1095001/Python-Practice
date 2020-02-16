import unicodedata

#TODO 判断输入的内容是不是数字

x = input('请输入一个数')
x = float(x)

if x < 0:
    print('你输入的是一个负数')
    pass
elif x > 0:
    print('你输入的是一个正数')
    pass
else:
    print('你输入的是0')
    pass
