# Write a Python program to drop microseconds from datetime.

import datetime

tday = datetime.datetime.today()#.replace(microsecond=0)
print(tday)