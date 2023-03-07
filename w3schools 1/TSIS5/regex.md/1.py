import re

file = open('C:/Users/Lenovo/pp2/w3schools 1/TSIS5/regex.md/row.txt', 'r', encoding="UTF8")


#1
# result1 = re.findall(".*a.*b*.*", file.read())
# print(result1)

# #2
# result2 = re.findall(".*a.*b.*b.*", file.read())
# print(result2)

#3
# result3 = re.findall(".*[\w]+[\-]+.*", file.read())
# print(result3)

#4
# result4 = re.findall('^[А-Я|A-Z][a-z|а-я]*.*', file.read())
# print(result4)

#5
result5 = re.findall('.*a+.*$b', file.read())
print(result5)