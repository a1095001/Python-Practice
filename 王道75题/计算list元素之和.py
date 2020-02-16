list1 = [11, 5, 17, 18, 23]
list2 = [23, 65, 19, 90]
list3 = [12, 15, 3, 10]
list4 = [1, 2, 3, 4, 5, 6, 7]
list1.extend(list2 + list3 + list4)
list1 = sorted(list1)
summery = 0
for i in list1:
    summery += i
    pass
print(summery)