import re
str = "this is a variable name"
result = re.sub('\s', '_', str)
print(result)
