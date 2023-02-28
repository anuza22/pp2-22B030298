# Write a Python program to print yesterday, today, tomorrow.
import datetime

tday = datetime.date.today()

yday = (tday-datetime.timedelta(days=1))
tomday = (tday+datetime.timedelta(days=1))

print("yesterday:", yday,'today:', tday,'tomorrow:', tomday)
