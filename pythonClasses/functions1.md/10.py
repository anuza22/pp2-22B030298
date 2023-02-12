a = [int(i) for i in input().split()]

def unique (a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b

b = unique(a)
for i in b:
    print(i, end=' ')