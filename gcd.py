num1=int(input("enter the no"))
num2=int(input("enter the no"))
if num1<num2:
    small= num1
else:
    small=num2
for i in range(1,small+1,1):
    if(num1%i==0 and num2%i==0):
        gcd=i
print("gcd is:",gcd)