check=[]
num=int(input("enter the size of the list"))
for i in range(0,num,1):
    check.append(int(input("enter the value:")))
print(check)
rar=0
for rar in check:
    if rar%2==0:
        print(" is a even no",rar)
    else:
        print(" is a odd no",rar)