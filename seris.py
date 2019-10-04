name= input("")
for i in range(0,len(name)-1,1):
    if(name[i]>name[1+i]):
        flag=10
        break
if(flag==0):
    print("is the seris")
else:
    print("not the seris")