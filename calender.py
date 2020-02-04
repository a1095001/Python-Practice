import calendar
calendar.setfirstweekday(firstweekday=0)   # 设置每周的第一天是周几（0 = Mo , 1 = Tu 以此类推）
yy = int(input('input years:'))
# mm = int(input('input month:'))
for i in range(12):                    # 显示出一年 12 个月份的日历
    print(calendar.month(yy, i + 1))   # 
    print('*' * 20)