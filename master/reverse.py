num = int(input('list的元素个数：'))
'''
# 倒序遍历
array = [num for num in range(1, num+1)]
array_reverse = [num for num in range(num, 0, -1) ]
print('翻转前：\n', array, '\n' '翻转后：\n', array_reverse)

'''

'''
# 使用内置reversed函数
array = [num for num in range(1, num+1)]
array_reverse = list(reversed(array))
print('翻转前：\n', array, '\n' '翻转后：\n', array_reverse)
'''

array = [num for num in range(1, num+1)]
array_reverse = array[::-1]
print('翻转前：\n', array, '\n' '翻转后：\n', array_reverse)