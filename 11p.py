#encoding = GBK
import math
import time

def user_input():
    input_list = []
    # a*x^2 + b*x + c = d
    # for correctly result, a should be 1, by now
    #a = float(input('Please input the first mumber: '))
    b = float(input('Please input the second mumber: '))
    c = float(input('Please input the third number: '))
    #d = float(input('And result: '))
    e = abs(b / 2)
    f = (e)**2
    input_list = [c,e,f]
    return input_list

def user_funtion(resource):
    result = []
    u = resource[2] - resource[0]
    if u < 0:
        return 0
    X = math.sqrt(u)
    Y = 0 - X
    x = resource[1] + X
    y = resource[1] + Y
    result = [x,y]
    return result

def user_output(result):
    print ('Then we have',result[0],'and',result[1])

def main():
    while(1):
        data = user_input()
        if data[0] == 0:
            return 0
        else:
            data_result = user_funtion(data)
            user_output(data_result)

start = time.time()
main()
end = time.time()
print('-----spent',end-start,'seconds-------')