import re

file = open('C:/Users/Lenovo/pp2/w3schools 1/TSIS5/regex.md/row.txt', 'r', encoding="UTF8")

result3 = re.findall(".*[\w]+[\-]+.*", file.read())
print(result3)

