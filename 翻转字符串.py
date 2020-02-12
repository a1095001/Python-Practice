str_1 = "www.s-keyman.site"

# 方法一：
i = len(str_1) - 1
str_list = []
while(i >= 0):
    str_list.append(str_1[i])
    i = i - 1
print(''.join(str_list))

# 方法二：
print(str_1[::-1])

# 方法三：
print(''.join(list(reversed(str_1))))