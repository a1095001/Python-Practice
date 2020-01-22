# Python 程序用于检测用户输入的数字是质数还是合数
import math

# 质数大于 1
def judge_prime(num):
    if num > 1:
        # 找到其平方根（ √ ），减少算法时间
        square_num = math.floor( num ** 0.5 )
        # 查找其因子
        for i in range(2, (square_num+1)): #将平凡根加1是为了能取到平方根那个值
            if (num % i) == 0:
                '''print(num, "是合数")
                print(i, "乘于", num // i, "是", num)'''
                return False
        else:
            #print(num, "是质数")
            # 如果输入的数字小于或等于 1，不是质数
            return True
    else:
        #print(num, "既不是质数，也不是合数")
        pass

# 用户输入数字
#num = int(input("请输入一个数字: "))
bouldery = int(input('请输入一个范围'))
prime_list = []
flag = False
temp = 0
for i in range(1 , bouldery , 1):
    temp = i
    flag = judge_prime(i)
    while flag == True:
        prime_list.append(temp)
        flag = False
        pass
    else:
        pass
    break
print(prime_list)