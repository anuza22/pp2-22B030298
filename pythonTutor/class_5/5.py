#«Первое и последнее вхождения»
a = input()

b = a.find('f')
c = a.rfind('f')

if b!=c and b!=-1: print(b, c)
elif b==c and b!=-1: print(b)
else: print()
