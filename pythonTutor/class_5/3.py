#«Две половинки»
import math
a = str(input())
b = a[:math.ceil(len(a)/2)]
c = a[math.ceil(len(a)/2):]
print(c+b)
