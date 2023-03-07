import re

res = input()

result = re.sub(r'(\w)([A-Z])', r'\1 \2', res)
print(result) 