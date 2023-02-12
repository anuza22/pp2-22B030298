a = [int(i) for i in input().split()]

def filter_prime(i):
    cnt = 0
    for j in range(1, i+1):
        if i%j==0: cnt+=1
    if cnt>2 or i==1: return False
    return True

for i in a:
    if filter_prime(i)==True:
        print(i, end=' ')