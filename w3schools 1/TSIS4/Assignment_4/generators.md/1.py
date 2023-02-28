def square(a):
    for i in range(a):
        yield i**2

for i in square(int(input())):
    print(i)