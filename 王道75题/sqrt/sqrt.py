import math
import cmath

x=float(input('输入要开方的数'))
if x<0:
    print('请输入大于0的正数')
    input('输入回车键结束程序')
x=math.sqrt(x)
print('所求结果为： %.2f' %(x))