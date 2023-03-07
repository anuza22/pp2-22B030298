import re

res = input()

result = re.sub("_", " ", res)
result= result.title()
result = re.sub(" ", "", result)

print(result)
