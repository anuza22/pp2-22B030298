# Write a Python program to convert degree to radian.

# Input degree: 15
# Output radian: 0.261904

import math

def convert(a):
    return a*math.pi/180

print(convert(float(input())))