'''
#方法一：使用内置函数
print(max(1,2))
'''
#方法二：建立list然后使用max函数
import unicodedata

def is_int(temp):
    try:
        int(temp)
        return True
    except ValueError:
        return False
    try:
        for i in temp:
            unicodedata.numeric(i)
        return True
    except(TypeError , ValueError):
        pass
    return False

mylist = []
temp = input('请输入数字构建list，输入s结束  ')
while temp != 's':
    if is_int(temp) == True:
        int(temp)
        mylist.append(temp)  #使用 append 一次只能添加一个对象到list末尾，且不产生新的list'''
        temp = input('请继续输入数字构建list，输入s结束  ')
        pass
    else:
        print('非法输入，请重新输入合法值')
    pass
else:
    print('最大的数字是：' , max(mylist))