#«Стоимость покупки»
a = int(input())
b = int(input())
n = int(input())

a = a*n

if b*n>=100:
    a+=b*n//100
    b=b*n%100
else: b = b*n

print(a, b)
