import os

with open(r"C:\Users\Lenovo\pp2\w3schools 1\TSIS6\dir-and-files.md\test.txt") as f:
    data = f.read()

print(data)

with open('C:/Users/Lenovo/pp2/w3schools 1/TSIS6/dir-and-files.md/test1.txt', 'w') as f2:
    f2.write(data)