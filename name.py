name=input("enter your name")
a=n=0
for i in name:
    if(i==' '):
        print(name[a].upper(),'.',end="")
        a=n
    n+=1
print(name[a::])
