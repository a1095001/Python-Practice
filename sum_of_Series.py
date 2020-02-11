def sum_of_series(num):
    sum = 0
    for i in range(1, num+1):
        sum = sum + i**3
        pass
    return sum
print(sum_of_series(100))