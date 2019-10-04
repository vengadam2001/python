import re
name=input("enter your name")
print("from the letters below find a meaningful word")
check=name
name=re.findall(r'\w',name)
if len(name)%2!=0:
    name.append(" ")
l=len(name)
for j in range(2):
    for i in range(j,l-j,2):
        temp=name[i]
        name[i]=name[i+1]
        name[i+1]=temp
print(name)
ch=input("enter the answer(the word found)")
if(check==ch):
    print("good you know your name")
else:
    print("wrong answer")
