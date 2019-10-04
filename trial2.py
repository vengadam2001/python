pi=3.14
print("what area do you want to find\n rect\n square\n circle")
shape=input("enter the shape")
if(shape=="rect"):
    a=float(input("enter the length"))
    b=float(input("enter the breath:"))
    print("teh area is:",a*b)
            
elif(shape=="square"):
            a=float(input("enter the side length"))
            print("the area is:",a*a)

elif(shape=="circle"):
            rad=float(input("enter the radius:"))
            print("area is:",2*pi*rad)

else:
            print("enter the correct area")
