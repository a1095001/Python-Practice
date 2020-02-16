import numpy

def fanzhuan(arr,d):
    arr = arr[d:] + arr[:d]
    return arr

arr = numpy.random.randint(1, 1000, 30)
arr = sorted(arr)
print('翻转前：', arr)
print('翻转后')
print(fanzhuan(arr,2))