a = [int(i) for i in input().split()]

def spy_game(a):
    for i in range(len(a)-2):
        if a[i]==0 and a[i+1]==0 and a[i+2]==7:
            return True
    return False

print(spy_game(a))