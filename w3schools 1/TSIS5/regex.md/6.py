import re

res = input()

result = re.sub('[\s\,\.]', ':', res)

print(result)
