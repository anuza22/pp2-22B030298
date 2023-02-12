import pyforest
from math import*
import numpy as np 
from matplotlib import pyplot as plt 

a = str(input("Function: ")) # write like example: pow= x**3, x**2 or sqrt=x**0.5
#numInt, upBnd, lowBnd = map(float, input().split())
numInt = float(input("Number of subintervals: "))
upBnd = float(input("Upper limit: "))
lowBnd = float(input("Lower limit: "))

delX = round((upBnd-lowBnd)/numInt, 5)
trap = 0
cnt = 0

for i in np.arange(lowBnd, upBnd+delX, delX, float):
    if i==lowBnd or i==upBnd or cnt==0 or cnt==numInt:
        trap+=delX*(eval(a, {"x": i })/2)
        if cnt==numInt: break
    else:
        trap+=delX*(eval(a, {"x": i}))
    
    cnt+=1
    
    
print(trap)

x = np.arange(lowBnd, upBnd+delX, delX)

y = eval(a, {"x": x})

plt.title("Trapezoidal Rule Calculator") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
#plt.plot(x,y) 
plt.plot(x, y)
plt.plot(x, y, 'ob')
plt.fill_between(x, y, 0,
                 facecolor="orange", # The fill color
                 color='blue',       # The outline color
                 alpha=0.2)          # Transparency of the fill
plt.show()

