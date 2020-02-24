# 方法一：左边的数比右边大
for x in range(1, 10):
    for y in range(1, 10):
        print('{}*{}={}'.format(x, y, y * x), end='\t')
    print()

# 方法二：左边的数比右边小
n=9
for row in range(1,n+1):  
    for col in range(1,row+1):
        print("{0}x{1}={2}".format(col , row , row*col),end='\t')
    print()