#将以数输出指定的日期

months = [
    'Jan',
    'Feb',
    'Mar',
    'Apl',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec'
]

endings = ['st', 'nd', 'rd'] + 17 * ['th']\
        + ['st', 'nd', 'rd'] + 7 * ['th']\
        + ['st']

year    = input('Year：')
month   = input('Month(1-12)')
day     = input('Day(1-31):')

monthnum = int(month)
daynum   = int(day)

#将表示月和日的数减1，这样才能得到正确的索引
month_name = months[monthnum - 1]
ordinal = day + endings[daynum - 1]
print(year + '.' + month_name + '.' + ordinal)