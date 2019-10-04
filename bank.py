class account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance= balance
    def deposit(self):
        amt=float(input("ennter the amount:"))
        self.balance+=amt
        print("current balance is:",self.balance)
    def withdraw(self):
        amt=float(input("enter the amount"))
        if amt>self.balance:
            print("low balance not enough money")
        else:
            self.balance-=amt
            print("the withdrawed amount is:",amt)
            print("the balance is",self.balance)
    def bal(self):
        print("your balance is:",self.balance)
name=input("enter your name:")
a=account(name)
while True:
    print("enter d to deposit the amount")
    print("enter w to withdraw")
    print("enter b to check the balance")
    print("enter 0 to exit")
    ch=input("enter your choice:")
    if ch=='W' or ch =='w':
        a.withdraw()
    elif ch=='D' or ch=='d':
        a.deposit()

    elif ch=='0':
        exit(-1)
    elif ch=='b' or ch=='B':
        a.bal()
    else:
        print("enter the correct choice")
