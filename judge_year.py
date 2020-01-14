#判断输入的年份是不是闰年

import unicodedata

def is_int(year):
    try:
        int(year)
        return True
    except ValueError:
        return False
    try:
        for i in year:
            unicodedata.numeric(i)
        return True
    except(TypeError , ValueError):
        pass
    return False

year = input('请输入需要查询的年份：')
flage = is_int(year)
while flage == False:
    print('非法输入！')
    year = input('请重新输入合法年份：')
    flage = is_int(year)
    pass
else:
    year = int(year)
    if year % 100 == 0:
        if year % 400 == 0:
            print('{} 年是闰年！'.format(year))
            pass
        else:
            print('{} 年是平年！'.format(year))
            pass
        pass
    else:
        if year % 4 == 0:
            print('{} 年是闰年！'.format(year))
            pass
        else:
            print('{} 年是平年！'.format(year))