#«Ход короля»
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a==c or a+1==c or a-1==c) and (b+1==d or b-1==d or b==d):
    print("YES")
else: print("NO")