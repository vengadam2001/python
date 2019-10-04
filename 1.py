str=''
import re
name=input("enter your name")
list1=name.split()
for i in range(len(list1)-1):
    if re.search('l',i):
        print(i)
print(str)
