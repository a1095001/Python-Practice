import calendar

def week(weekday):
    switcher = {
        0:'周一',
        1:'周二',
        2:'周三',
        3:'周四',
        4:'周五',
        5:'周六',
        6:'周日',
    }
    return switcher.get(weekday)

year , month = map(int, input('请输入要查询的年月：').split(' '))
monthRange = calendar.monthrange(year , month)
weekday = week(monthRange[0])
days = monthRange[-1]
print(f'{year}年{month}月的第一天是{weekday}，本月共{days}天。')