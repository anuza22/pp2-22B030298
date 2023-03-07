import re

res = input()

result = re.findall('^[А-Я|A-Z]+[a-z|а-я]+', res)


print(*result)