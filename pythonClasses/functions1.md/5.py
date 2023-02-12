import itertools

a = input()

def permut(a):
    b = set([''.join(i) for i in itertools.permutations(a)])
    return b

print(permut(a))