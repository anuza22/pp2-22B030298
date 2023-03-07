import re

res = input()

result = re.split("\s", res)

for i in range(len(result)):
    result[i]=result[i].title()

print(result)
