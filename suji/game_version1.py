# Done 做成猜数字游戏
# Done 退出功能（错i次后）
#第一版游戏

import random
import time
import sys

temp = int(input('请输入猜测的整数（0-100）'))
ans  = random.randint(0,100)
i = 0
while (temp != ans) :
    if i == 5:
        i = 0
        print('很遗憾你已经用完了5次机会，游戏将在1S后退出')
        time.sleep(1)
        exit(0)
        pass
    if temp > ans:
        i = i + 1
        print('很遗憾，猜错了！你输入的数字比答案大')
        temp = int(input('请再次输入猜测的整数（0-100）：\n'))
        pass
    elif temp < ans:
        i = i + 1
        print('很遗憾，猜错了！你输入的数字比答案小')
        temp = int(input('再次输入猜测的整数（0-100）：\n'))
        pass
else:
    print('恭喜你，猜对了！！！')
    input('按下回车键退出')