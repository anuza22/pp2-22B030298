#«Конец уроков»
a = int(input())
minut = int()
n = a

while a!=0:
    if a%2==0 : minut+=15
    else: minut+=5
    
    minut+=45
    a-=1

if n%2==0: minut-=15
else: minut-=5

hour = 9+minut//60
m = minut%60

print(hour, m)
