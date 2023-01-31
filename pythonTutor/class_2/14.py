#«Сколько совпадает чисел»
a = int(input())
b = int(input())
c = int(input())

d = {a, b, c}

if len(d)==3:
    print(0)
else:
    print(4-len(d))
