# 在 Windows 下，文件路径前需要加 r 取消 \ 转义或者将 \ 用 \\ 转义，否则会转码错误。

'''文件IO'''
with open(r'C:\Users\Keyma\Desktop\s.txt','wt') as fileout:
    fileout.write("写一行中文试试\n")
with open(r'C:\Users\Keyma\Desktop\s.txt','rt') as filein:
    print(filein.readline())