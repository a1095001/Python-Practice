# 使用循环实现计算 n 个自然数的立方和
def sum_of_series(num):
    summery = 0
    for i in range(1, num+1):
        summery = summery + i**3
        pass
    return summery
print(sum_of_series(100))