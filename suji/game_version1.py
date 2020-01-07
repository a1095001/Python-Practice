# Done 做成猜数字游戏
#第一版游戏

import random

temp = int(input('请输入猜测的整数（0-10）'))
ans  = random.randint(0,10)
while (temp != ans) :
    if temp > ans:
        print('很遗憾，猜错了！你输入的数字比答案大')
        temp = int(input('请再次输入猜测的整数（0-10）：\n'))
    elif temp < ans:
        print('很遗憾，猜错了！你输入的数字比答案小')
        temp = int(input('再次输入猜测的整数（0-10）：\n'))
else:
    print('恭喜你，猜对了！！！')
    input('按下回车键退出')