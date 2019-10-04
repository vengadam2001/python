filename=input("enter the filename:")
a=input("enter the character to be searched:")
file=open(filename,'r')
count=0
for i in file.read():
    if i==a:
        count+=1
print("the no of times ",a," repeated is ",count)