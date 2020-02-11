# 创建一个空的list
li = []
print(li)

# 创建一个list
li = ["a", "b", "mpilgrim", "z", "example"]
print(li)

# 选中list中元素(顺序从0开始)
print(li[1])

# list负数索引(-1为最后一个元素，-2为倒数第二个元素，以此类推)
print(li[-1])
print(li[-4])

# 第二到倒数第二个元素（左闭右开区间）
print(li[1 : -1])

# 增加元素
li.append('new')
print(li)
li.insert(3, 'new')
print(li)
li.extend(['c','two'])
print(li)

# 搜素元素
print(li.index('new'))
print("c" in li)

# delete the element
print(li.remove('two'))
print(li.remove('new'))                                                          # 删除首次出现的一个值,第二个 'new' 未删除
print(li)
print(li.pop())                                                                  # pop 会做两件事: 删除 list 的最后一个元素,然后返回删除元素的值
print(li)

# list 运算符
li = ['a', 'b', 'mpilgrim']
print(li + ['example', 'new'])
li += ['two']
print(li)
li = [1,2]*3
print(li)

# 使用join链接list成为字符串
params = {
        "server":"mpilgrim",
        "database":"master",
        "uid":"sa",
        "pwd":"secret"
}
'''
  通过遍历params这个字典里的key和values来创建一个list，元素由"key=values"组成  
  效果：['server = mpilgrim', 'database = master', 'uid = sa', 'pwd = secret']
'''
print(["%s = %s" % (key , values) for key, values in params.items()])             
print(";".join(['%s = %s' % (key, values) for key, values in params.items()]))    # 使用";"来分割list，并转换为字符串

# list 分割字符串
li = [
    'server=mpilgrim',
    'uid=sa',
    'database=master',
    'pwd=secret'
]
# 使用";"来分割list，并转换为字符串
s = ";".join(li)
print(s)
# split函数与join函数相反
print(s.split(";"))
# split(sep=None, maxsplit=-1)：sep为分割的标志字符或字符串；maxsplit为分割次数（默认为-1，既全部）
print(s.split(';', 1))

# list 的映射解析
li = [1, 9, 8, 4]
# li里面的每个元素×2之后输出，不改变li
print([elements*2 for elements in li])
print(li)
# 将li的每个元素×2之后重新赋值给li
li = [element*2 for element in li]
print(li)

# dictionary 中的解析
params = {
        "server":"mpilgrim",
        "database":"master",
        "uid":"sa",
        "pwd":"secret"
}
# dict.keys()的返回值不一定是原字典的顺序
print(params.keys())
# dict.values()的返回值一定是与keys()返回值一一对应，即keys == values
print(params.values())

# list 过滤
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
# for 循环遍历 li
print([elem for elem in li if len(elem) > 1])
print([elem for elem in li if elem != "b"])
print([elem for elem in li if li.count(elem) == 1])
# list 映射解析的实现
list1 = []
for elem in li:
        if li.count(elem) == 1:
                list1.append(elem)
print(list1)