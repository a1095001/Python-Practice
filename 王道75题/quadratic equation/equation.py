# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0

# 导入 cmath(复杂数学运算) 模块
import math

a=int(input('请输入a的值'))
b=int(input('请输入b的值'))
c=int(input('请输入c的值'))

#判断
if a == 0:
    if b == 0:
        print('这不是方程，不需要解')
    else:
        x = -c / b
        float(x)
        print('这是一元一次方程，解得：x=', x)
elif a != 0:
    if b == 0:
        x = math.sqrt(-c / a)
        print('解得：x=', x)
    else:
        d = (b**2) - (4*a*c)
        if d < 0:
            print('方程无实数解')
        elif d > 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print('解得：x1={0}\n x2={1}'.format(x1 , x2))
