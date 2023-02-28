def square(a, b):
    for i in range(a, b):
        yield i**2

a, b = map(int, input().split())

c = square(a, b)

for i in range(b-a+1):
    print(next(c))