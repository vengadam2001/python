import re
str1=input("enter the string")
str2=re.findall(r'\w+',str1)
str3=re.findall(r'\w',str2[0])
j=0
for i in str3:
    if not re.search("\d",i):
        j=10
        break
if j==0 and (re.search("[A-Z]",str2[1])  or re.search("[a-z]",str2[1])):
    print("format correct")
else:
    print("format incorrect")
