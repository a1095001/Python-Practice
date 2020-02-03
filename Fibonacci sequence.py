# 使用循环语句实现斐波那契数列(第0项是0)

n1 = 0
n2 = 1
# 数列第一、二项
fibonacci = [n1 , n2]
nterms = int(input('你需要几项：'))
while nterms <= 0:
    nterms = int(input('请重新输入一个正整数：'))
    pass
if nterms == 1:
    print(fibonacci)
    pass
else:
    for count in range(1 , nterms - 2 , 1):
        element = n1 + n2
        # reflash the value
        n1 = n2
        n2 = element
        # [list_name].append(element)函数往 list 末尾添加一个元素
        fibonacci.append(element)
        pass
    print(fibonacci)