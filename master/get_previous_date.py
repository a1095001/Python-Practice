import datetime
from numpy import random

d = random.randint(0, 15)
date = datetime.datetime.now() - datetime.timedelta(days = d)
print(date)