import re
str1='ray'
result=re.findall(r'[aeiouAEIOU]y$',str1)
print(result)
print(str1)