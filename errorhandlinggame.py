'''class valuetoolarge(Exception):
    def display(self):
        print("value too large")
class valuetoosmall(Exception):
    def display(self):
        print("value too low")
max=100
while True:
    try:
        g=int(input("enter the no:"))
        if(g>100):
            raise valuetoolarge
        elif(g<100):
            raise valuetoosmall
        else:
            print("you are correct")
            break
    except valuetoolarge as s:
        s.display()
    except valuetoosmall as k:
        k.display()
    finally:
        print("i am finally")
'''
'''

while True:
    try:
        a=int(input("enter the number"))
        print("the area is",a**2)
    except ValueError:
        print("enter the data in correct data type")
    else:
        break
'''
'''
class agetoolow(Exception):
    def display(self):
        print("not elegible age is low")
try:
    g=int(input("enter the age"))
    if g<18:
        raise agetoolow
    else:
        print("you are eligible")
except agetoolow as a:
    a.display()

'''
'''
class ilarge(Exception):
    def disp(self):
        print("the seris is over")
try:
    i=int(input("enter teh no"))
    for j in range(i,i+34,1):
        if j<30:
            print(j*5)
        else:
            raise ilarge
except ilarge as a:
    a.disp()
'''
try:
    file=open("text.txt",'r')
    sum=int(input())+(input())
    file.write("")
except IOError:
    print("hello")
except TypeError:
    print("helloqqw")

