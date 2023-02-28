def even(a):
    for i in range(1, a):
        if i%2==0:
            yield i

for i in even(int(input())):
    print(i, end = ", ")