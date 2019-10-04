''''import re'''
'''
import re as r
str=input("enter the str")
pattern=input("enter the value for match")
if r.search(pattern,str):
    print("match found")
else:
    print("not found")
'''
'''write a programme that checks if the string has at least one vowels'''
'''import re
pattern=r"[aeiou]"
word=input("enter the word")
if re.search(pattern,word):
    print("vowels is there")
else:
    print("not found")'''
'''write a programme that validates your mobile number the no should start with 6 7 8 9 followed by 9 digits'''
'''import re
list=["7238965943","8559999544"]
for i in list:
    result = re.findall(r'[6-9]{1}[0-9]{9}', i)
    if result:
        print(result)'''
'''write a programme that prints only those words that start with vowels'''
'''
import re
str1="are you fine do you need a umbralla"
str2 = re.findall(r'\b[aeiouAEIOU]\w+',str1)
print(str2)
'''
'''
\ b matches the word boundary
\w matches word character
^ matches at the begining of the line
$ matches at the end of the line
. matches any single character except the new line character


write a programme to print the last word start with vowels

write a programme to print the begining of the line that starts with vowels
'''
import re
list1=["7238969943","85599544"]
print(len(list1[0])+10)
result = re.findall("\b", list1[0])
print(result , list1)

