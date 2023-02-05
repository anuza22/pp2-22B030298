#«Проценты»
a = float(input())
b = float(input())
c = float(input())

k = (b+c/100)*(1+a/100)
b = int(k)
c = k*100%100
print(b, int(c))
