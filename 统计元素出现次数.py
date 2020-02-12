'''
# 方法一：遍历数组后输出
array = [15, 6, 7, 10, 12, 20, 10, 28, 10]
search_ele = int(input('请输入想要查询的数字：'))
count = 0
for ele in array:
    if ele == search_ele:
        count += 1
        pass
    pass
print(f'查询的数字{search_ele}在list中出现了{count}次')
'''

# 方法二：使用count()方法
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
print('数字8在list中出现了', lst.count(8), '次')

