str_1 = "www.s-keyman.site"
def rotate(input,d): 
    # 截取头d个字符串
    Lfirst = input[:d]
    # 截取从d到末尾的字符串
    Lsecond = input[d:]
    Rfirst = input[:len(input)-d] 
    Rsecond = input[len(input)-d:] 
    print( "头部切片翻转 : ", (Lsecond + Lfirst) )
    print( "尾部切片翻转 : ", (Rsecond + Rfirst) )

print(rotate(str_1, 4))
