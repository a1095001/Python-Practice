def index_of_str(s1, s2):
    #split这个 函数分割字符，返回的 是分割后的元素组成的列表
    lt=s1.split(s2)
    #判断分割后的列表的元素个数，如果元素个数为一个，说明列表中只有一个元素，证明s1中没有s2的字符
    if len(lt) == 1:
        return -1
    #多于一个元素，证明是分割了。用index函数求出s2元素在列表中的下标
    else:
        return s1.index(s2)
s1="www.google.com"
s2="google"
index_of_str(s1,s2)
print(index_of_str(s1,s2))