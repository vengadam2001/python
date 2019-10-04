import re
str1= input("enter a word")
if re.search(r'[aeiou]y$',str1):
    str1 = re.findall('\w', str1)
    str1.append('s')
elif re.search(r'y$',str1):
    str1 = re.findall('\w',str1)
    str1.pop()
    str1.append("ies")
elif re.search(r'f$',str1):
    str1 = re.findall('\w',str1)
    str1.pop()
    str1.append("ves")
elif re.search(r'fe$',str1):
    str1 = re.findall('\w',str1)
    str1.pop()
    str1.pop()
    str1.append("ves")
elif re.search(r's$',str1) or re.search(r'ch$',str1) or re.search(r'sh$',str1) or re.search(r'ss$',str1) or re.search(r'x$',str1) or re.search(r'z$',str1) or re.search(r'o$',str1):
    str1 = re.findall('\w',str1)
    str1.append("es")
elif re.search(r'us$',str1):
    str1 = re.findall('\w',str1)
    str1.pop()
    str1.pop()
    str1.append("i")
elif re.search(r'is$',str1):
    str1 = re.findall('\w',str1)
    str1.pop()
    str1.pop()
    str1.append("es")
elif re.search(r'on$',str1):
    str1 = re.findall('\w',str1)
    str1.pop()
    str1.pop()
    str1.append("a")
else:
    str1 = re.findall('\w',str1)
    str1.append('s')

str2=''
for i in str1:
    str2+=i
print(str2)
