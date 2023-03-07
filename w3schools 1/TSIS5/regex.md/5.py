import re

res = input()

result = re.findall('.*a*.*b$', res)


print(*result)

