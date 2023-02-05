#«Второе вхождение»
a = input()

if a.count("f")==1:
    print(-1)
elif a.count("f")==0:
    print(-2)
else:
    k = a.find("f")
    print(a.find("f", k+1, len(a)))
