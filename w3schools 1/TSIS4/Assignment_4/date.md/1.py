# Write a Python program to subtract five days from current date.

import datetime

tday = datetime.date.today()
w = datetime.timedelta(days=5)
print(tday-w)

