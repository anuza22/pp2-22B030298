def numbers(a):
    for i in range(a, 0, -1):
        yield i

for i in numbers(int(input())):
    print(i)