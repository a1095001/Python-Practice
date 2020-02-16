#用户输入数字
num1=input('请输入第一个数字')
num2=input('请输入第二个数字')
nsum=float(num1) + float(num2)
#格式化输出   print('数字{0}和数字{1}相加结果为：{2}'.format(num1,num2,nsum))
#            按照{0}，{1}，{2}的顺序输出（内容分别为num1,num2,nsum）
print('数字{0}和数字{1}相加结果为：{2}'.format(num1,num2,nsum))
input('请输入回车键')