'''
定理：x、y 两个数的最小公倍数乘以它们的最大公约数等于 x 和 y 本身的乘积。
即LCM(x,y)=(x*y)/GCD(x,y)
'''

num1, num2 = map(int, input('请输入两个非零自然数：').split(' '))
# print(isinstance(num1, int))
# print(isinstance(num2, int))
while num1 & num2 == 0:
    num1, num2 = map(int, input('非法输入！请重新输入两个非零自然数：').split(' '))
    pass
else:
    temp1 , temp2 = num1 , num2
    product = num1 * num2
    if num1 == 0:
        num1, num2 = num2, num1
        pass
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    GCD = num1
    LCM = product / GCD
    pass
print(f'{temp1}和{temp2}的最小公倍数是{LCM}')
