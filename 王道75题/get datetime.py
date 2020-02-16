import datetime

getday = datetime.date.today()
yesterday = datetime.timedelta(days = 1)
getyesterday = getday - yesterday
print('昨天是：', getyesterday)