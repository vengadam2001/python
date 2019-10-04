from test6module import *
filename=input("enter the filename")
list1=[]
while True:
    list1.append(int(input("enter the no")))
    ch=input("do you want to continue")
    if ch=='n'or ch=='N':
        pos(list1,filename)
        break
f=open(filename,"r")
print("the no of positive no is:",f.read())