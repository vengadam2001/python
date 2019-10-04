ch='y'
while ch=='y':
    salary=float(input("enter the number"))
    gender=input("enter your gender(M/F)")
    if(salary<10000):
        if(gender=='M' or gender=='m'):
            bonus=salary*(7/100)
        elif(gender=='F' or gender=='f'):
            bonus=salary*(12/100)
    else:
        if(gender=='M' or gender=='m'):
            bonus=salary*(5/100)
        elif(gender=='F' or gender=='f'):
            bonus=salary*(10/100)
    print("\nthe bonus is :",bonus)
    print("the net salary(salary+sum) is:",bonus+salary)
    ch=input("do you wnat to continue(y/n)")