num = int(input('list的元素个数：'))
array = [num for num in range(1, num+1)]

'''
# 方法一：使用extend
array_clone = []
array_clone = array_clone.extend(array)
'''

'''
# 方法二：使用list
clone_array = list(array)
'''

'''
# 方法三
clone_array = array[:]
'''

# 方法四：使用copy
clone_array = array.copy()
print(array)
print(clone_array)