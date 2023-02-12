import numpy as np 
a = str(input())
numInt, upBnd, lowBnd = map(float, input().split())

delX = (upBnd-lowBnd)/numInt

from matplotlib import pyplot as plt 
x = np.arange(lowBnd, upBnd+delX, delX)
y = eval(a, {"x": x})
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
#plt.plot(x,y) 
 
plt.show()