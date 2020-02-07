def GetPlus(x , y):
    return x + y

def GetSubtraction(x , y):
    return x - y
def GetMultiplication(x , y):
    return x * y

def GetDivision(x , y):
    if y == 0:
        print('0不能作为分母！')
        return
    else:
        return x / y

def switcher(value):
    switcher = {
        0: 'GetPlus',
        1: 'GetSubtraction',
        2: 'GetMultiplication',
        3: 'GetDivision',
    }
    return switcher.get(value , 'wrong value')

choice = int(input('请选择模式：\n1:加法\n2:减法\n3:乘法\n4:除法\n'))
x , y = map(int, input('请输入要进行计算的两个数字：').split(' '))
result = switcher.get(x , y)
print(f'{x}和{y}的运算结果为:{result}')
