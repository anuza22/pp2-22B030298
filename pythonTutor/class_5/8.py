#«Обращение фрагмента»
a = input()
k = a.find("h")
k1 = a.rfind("h")

b = a[k1-1:k:-1]
a = a.replace(a[k+1:k1], b)
print(a)
