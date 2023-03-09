import re

file = open('row.txt', 'r', encoding="UTF8")

#2
result2 = re.findall(".*[a].*[b].*[b].*", file.read())
print(result2)

