#«Парты»

a = int(input())
b = int(input())
c = int(input())

num = 0

if a%2==0: num= num+a/2
else: num= num+ (a//2+1)

if b%2==0: num= num+b/2
else: num= num+ (b//2+1)

if c%2==0: num= num+c/2
else: num= num+ (c//2+1)
    

print (int(num))
