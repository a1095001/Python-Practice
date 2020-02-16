list1 = [11, 5, 17, 18, 23]
list2 = [23, 65, 19, 90]
list3 = [12, 15, 3, 10]
list4 = [1, 2, 3, 4, 5, 6, 7]
list1.extend(list2 + list3 + list4)
# sorted()返回一个序列，此处可用sort()  即list1.sort(),但要注意sort()返回None
list1 = sorted(list1)
print('最小元素为:', list1[0])

# 方法二：
print('最小元素为:', min(list1))