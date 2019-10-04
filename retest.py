'''import re
list=["7238965143","855544"]
for i in list:
    result = re.findall(r'[6-9]{1}[0-9]{9}',i)
    if result:
        print(result)'''
'''write a programme that uses a re to match string with start with a sequence of digit followed by a ' '(space) and after this character or string
write a prog that uses re to pluralise a word
'''
import re
result=re.findall(r'\b[aeiouAEIOU]\w+',"hello welcome to sret")
print(result)

result1=re.findall(r'\w+$',"good even")
print(result1)
