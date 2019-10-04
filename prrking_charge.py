typ=input("enter the type of your vechical.\n bike\n car \n suv \n truck")
if(typ=="bike"):
    time = float(input("enter the time in hrs"))
    cost=20*time
    print("cost is",cost)
elif(typ=="car"):
    time = float(input("enter the time in hrs"))
    cost = 30*time
    print("cost is",cost)
elif(typ=="suv"):
    time = float(input("enter the time in hrs"))
    print("the cost is",40*time)
elif(typ=="truck"):
    time = float(input("enter the time in hrs"))
    print("the cost for string is:",50*time)
else:
    print("enter the correct option")