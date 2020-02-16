fish = 6
# A醒来后能分第一次鱼，故鱼开始至少有6条
# fish_array = []
while True:
    total, enough = fish, True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1)  //  5 * 4
            # 计算剩余的鱼是否满足-1后剩余数量能整除5（循环5次都符合即为所求）
        else:
            enough = False
            # 跳出for循环，提高程序运行速度（没有这个break程序需要跑完5次for循环才能执行下一行代码）
            break
    if enough:
        get = total // 5
        fish_array = fish_array.append(get)
        print(f'总共有{fish}条鱼')
        '''
        print(f'A获得{fish_array[0]}条鱼\nB获得{fish_array[1]}条鱼\n\
                C获得{fish_array[2]}条鱼\n\
                D获得{fish_array[3]}条鱼\n\
                E获得{fish_array[4]}条鱼\n')
            '''
        # 跳出while循环，结束程序
        break
    fish += 1
