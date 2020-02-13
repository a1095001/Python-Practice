def search(array, s, n):
    for i in range(0, n):
        if (array[i] == s):
            return i
    return -1

array = [ 'A', 'B', 'C', 'D', 'E' ]
s = 'D'
n = len(array)
result = search(array, s, n)
if result == -1:
    print('元素不在数组中')
    pass
else:
    print('元素在数组中')