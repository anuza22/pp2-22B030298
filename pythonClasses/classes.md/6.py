a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
a = list(filter((lambda x: all(x%i!=0 for i in range(2,x))), a))
print(a)
