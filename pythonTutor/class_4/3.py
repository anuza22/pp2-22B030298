#«Ряд - 3»
import math
a = float(input())
b = int(input())

a = int(math.ceil(a/2)*2)

for i in range(a-1, b-1, -2):
    print(i, end=" ")
