x = input('Please input string for x:')
y = input('Please input string for y:')

temp = x
x = y
y = temp
print('交换后x的值为{0}\n交换后y的值为{1}'.format(x,y))