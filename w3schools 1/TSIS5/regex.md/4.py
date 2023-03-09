import re

# res = input()

# result = re.findall('^[А-Я|A-Z]+[a-z|а-я]+', res)


# print(*result)

file = open('row.txt', 'r', encoding="UTF8")

result = re.findall('.*[A-Z]+[a-z]+.*', file.read())

print(result)

