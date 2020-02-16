def reversal(list,n1,n2):
    temp = list[n1]
    list[n1] = list[n2]
    list[n2] = temp
    print(list)

list = [1,2,3,4,5,6,7]
print("对调前：",list)
reversal(list,4,5)
