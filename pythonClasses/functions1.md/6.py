a = input()

def reverse(a):
    b = a.split(' ')
    b = b[::-1]
    return b

print(a, "-->", end = ' ')
for i in reverse(a):
    print(i, end=' ')

