#«Ход слона»
import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())
k = bool(False)

"""if (a+b+c+d)%2==0: 
    k = True
else:
    print("NO")
    exit()"""

if abs(a-c)==abs(b-d): k = True
else: k = False

if k==True: print("YES")
else: print("NO")