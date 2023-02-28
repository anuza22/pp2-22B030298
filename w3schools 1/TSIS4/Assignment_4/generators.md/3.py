def divby_3and4(a):
    for i in range(1, a):
        if i%4==0 and i%3==0:
            yield i

for i in divby_3and4(int(input())):
    print(i, end = ", ")