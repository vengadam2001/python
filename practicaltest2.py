class emp:
    def __init__(self,name=[],desig=[],salary=[]):
            self.employeename = name
            self.employeedesig = desig
            self.employeesalary = salary
            self.count=len(name)
    def enter_details(self):
        while True:
            self.employeename.append(input("enter the name of the employee:"))
            self.employeedesig.append(input("enter the designation:"))
            self.employeesalary.append(float(input("enter the salary")))
            ch=input("do you want to continue")
            if ch=='n' or ch=='N':
                break
            else:
                pass
        return(self.count)
    def returnemp(self):
        return(self.count)
ob=emp()
while True:
    ch=input("enter your choice \nenter e to enter the details\nenter r to return the no of employees\nenter 0 to exit")
    if ch=='e':
        print(ob.enter_details())
    elif ch=='r':
        print("the no of employees are:",ob.returnemp())
    elif ch=='0':
        exit(-1)
    else:
        print("enter teh correct option")
