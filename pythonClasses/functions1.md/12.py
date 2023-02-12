a = [int(i) for i in input().split()]

def histogram(a):
    s = '*'
    for i in a:
        print(s*i)

histogram(a)

