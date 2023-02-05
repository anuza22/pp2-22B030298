#«Потерянная карточка»
a = int(input())
d=0
c=a

for i in range(1, a):
    b = int(input())
    c+=i
    d +=b
    
print(c-d)
