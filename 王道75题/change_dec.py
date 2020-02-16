# 以下代码用于实现十进制转二进制、八进制、十六进制(dec to bin,oct,hex)：

number = int(input('请输入要转换的数字：'))
print('十进制数为：' , number)
print('二进制数为：{:b}'.format(number))
print('八进制数为：{:o}'.format(number))
print('十六进制数为：0X{:X}'.format(number))