# 将列表的头尾两个元素对调
import numpy

def function (arr):
    a = arr.pop(0)
    b = arr.pop(-1)
    arr.append(a)
    arr.insert(0, b)
    return arr

arr = list(numpy.random.randint(1, 1000, 10))
print("调转前：", arr)
# 方法一：
arr[0], arr[-1] = arr[-1], arr[0]
print("法一调转后：", arr)

# 方法二：
temp = arr[0], arr[-1]
arr[0], arr[-1] = temp
print("法二调转后：", arr)

# 方法三：
print("法三调转后：", function(arr))
