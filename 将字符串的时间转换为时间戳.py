import os, time, datetime

a1 = "2020-2-10 23:40:00"
time_tuple = time.strptime(a1, "%Y-%m-%d %H:%M:%S")
timestamp = int(time.mktime(time_tuple))
print(timestamp)