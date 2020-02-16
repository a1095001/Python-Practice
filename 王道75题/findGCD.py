# 使用欧几里得算法求出两个数的最大公约数等于其中较小的那个数和两数相除余数的最大公约数。
# GCD(x,y)=GCD(y,x mod y),x>y

def gcd(a,b):
    if a == 0:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

num1 = int(input('请输入第一个正整数: '))
num2 = int(input('请输入第二个正整数: '))
print('{}和{}的最大公约数为: {}'.format(num1,num2,gcd(num1,num2)))