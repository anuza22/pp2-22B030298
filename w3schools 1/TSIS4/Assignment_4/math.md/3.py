# Write a Python program to calculate the area of regular polygon.

# Input number of sides: 4
# Input the length of a side: 25
# The area of the polygon is: 625

import math

def area(a, b):
    return a*b**2/(math.tan(math.pi/a)*4)

a = int(input('sides: '))
b = int(input('length of a side: '))
print(area(a, b))