# Write a Python program to calculate two date difference in seconds.

import datetime 

tday = datetime.date.today()
bday = datetime.date(2023, 2, 24)

print((tday-bday).total_seconds())