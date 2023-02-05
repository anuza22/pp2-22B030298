#«Часы - 3»
import math
a = float(input())
a = a/(360/(12*3600))

print(a//3600, (a%3600)//60, math.floor(a%3600%60))
