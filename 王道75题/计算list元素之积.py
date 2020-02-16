import functools
list1 = [11, 5, 17, 18, 23]
list2 = [23, 65, 19, 90]
list3 = [12, 15, 3, 10]
list4 = [1, 2, 3, 4, 5, 6, 7]
list1.extend(list2 + list3 + list4)
sorted(list1)

'''
# 方法一：
product = 1
for i in list1:
    product = product * i
    pass
'''

# 方法二：
def multiply(x, y):
    return x * y
product = functools.reduce(multiply, list1)
print(product)