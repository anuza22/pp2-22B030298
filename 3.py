import pyforest
from math import*
import numpy as np 
from matplotlib import pyplot as plt 
# def frange(start, stop=None, step=None):
#     # if set start=0.0 and step = 1.0 if not specified
#     start = float(start)
#     if stop == None:
#         stop = start + 0.0
#         start = 0.0
#     if step == None:
#         step = 1.0

#     count = 0
#     while True:
#         temp = float(start + count * step)
#         if step > 0 and temp >= stop:
#             break
#         elif step < 0 and temp <= stop:
#             break
#         yield temp
#         count += 1

a = str(input())
numInt, upBnd, lowBnd = map(float, input().split())

delX = (upBnd-lowBnd)/numInt
trap = 0

for i in np.arange(lowBnd, upBnd+delX, delX):
    if i==lowBnd or i==upBnd:
        trap+=delX*(eval(a, {"x": i, "sqrt":sqrt, "e":2.718 })/2)
    else:
        trap+=delX*(eval(a, {"x": i}))
    
print(trap)

x = np.arange(lowBnd, upBnd+delX, delX)

y = eval(a, {"x": x})

plt.title("Trapezoidal Rule Calculator") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 

plt.plot(x, y)
plt.plot(x, y, 'ob')
plt.show()

