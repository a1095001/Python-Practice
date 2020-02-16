#计算三角形面积（已知三边长求三角形面积）
#海伦公式：S=sqrt(p(p-a)(p-b)(p-c))  其中 q 为半周长，abc为三角形边长
# p = (a+b+c)/2

import math

def triangle():
    a = input('输入第一条边边长：')
    b = input('输入第二条边边长：')
    c = input('输入第三条边边长：')
    p = (a + b + c) / 2
    s = math.sqrt(p*(p - a)*(p - b)*(p - c))
    return s 

print('三角形的面积为：', triangle())