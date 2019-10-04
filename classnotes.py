''''#write a python programme to get a number if the number is <than 10 then add 5
n=int(input("enter a number"))
if(n<10):
    n+=5
    print(f"the num is{n}")
else:
    print("the number is:",n)'''
'''....................................................................................................................''''''
lis=[]
num=int(input("enter the no of elements:"))
for i in range(num):
    lis.append(int(input("enter teh element:")))
odd=[]
even=[]
for i in lis:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("the even nos are:",even)
print("the odd nos are:",odd)'''
'''............................................................''''''
num=[]
n=int(input("enter teh no of elemwnts"))
prime=[]
composite=[]
k=0
for i in range(0,n,1):
    num.append(int(input("enter the no")))
for j in num:
        for a in range(2,j,1):
            if j%a==0:
                k=10
        if k==0:
            prime.append(j)
        else:
            composite.append(j)
        k=0
print("teh prime nos are :",prime)
print("the composite no are :",composite)
'''
'''.................................................................'''
'''my_string=['s','a','m','m','y']
print("\ncontuinue\n")
for letter in my_string:
    if(letter=='a'):
        continue
    print("\n",letter)
print("\npass:\n")
for letter in my_string:
    if(letter=='a'):
        pass
    print("\n",letter)
print("\nbreak:\n")
for letter in my_string:
    if(letter=='a'):
        break
    print("\n",letter)
  ''' '''....................................................................'''
'''num=int(input("enter the no "))
a=num
sum=0
while a!=0:
    temp=a%10
    sum+=temp
    a//=10
print("\n the sum is:",sum)
''''''.........................................'''
'''num=int(input("enter the no "))
a=num
sum=0
while a!=0:
    temp=a%10
    sum=(sum*10)+(temp)
    a//=10
print("\n the reverse is:",sum)'''
'''
NOTES:-
lists can be scliced like strings...
mylist=[1:]
[two, three]
anathorlist=['five','six']
mylist+anotherlist
['one','two,'three','four','five','six']'''
'''
list1=(1,2,3,20,12,300,456,66)
print("\n",max(list1))
print("\n",min(list1))
print("\n",sorted((list1)))
#print("\n",list1.pop())
print("\n",3 in list1)
print("\n",200 not in list1)
print("\n",list1.pop(4))
print(list1[::-1])
'''
'''.......................................................................'''
'''24 aug 2019'''
'''ques=[]
ans=[]
flag = 0
while flag == 0:
    ques.append(input("enter the question"))
    ans.append(input("enter the answer"))
    ch=input("do you ant to continue")
    if(ch == 'n' or ch =='N'):
        flag=1
for q,a in zip(ques,ans):
    print('\n',q,'?')
    print(a)
ques=["WHAT IS YOUR NAME","WHAT DO YOU DO IN YOUR LESURE TIME","WHAT DO YOU LIKE TO EAT WHEN YOU ARE TIERD"]
ans=[]
for i in range(0,len(ques),1):
    print(ques[i],"?")
    ans.append(input("enter the answer"))
for q,a in zip(ques,ans):
    print('\n',q,'?')
    print(a)'''
                                #dictinory

'''write a programme that has a set of words in english words and corresponding words in hindi'''
'''define another dict that has alist of words in hindi and the corresponding words in urudu'''
'''take all words from english lang and display their meanings in both the lang '''
'''
d={"regno":1234,"name":"thiru","mobile":12345678}
print(d)
'''
'''
eh={"friend":"dhosth","food":"kana","book":"kithab"}
ht={"dhosth":"shahithu","kana":"haharam","kithab":"gratham"}
for i in eh:
    print(i,"in hindi is",eh[i],"in telagu is",ht[eh[i]])
'''
'''write a python programme to print the frequency of character occuring in a message'''
'''
msg=input("enter teh message")
msg=msg.lower()
d=dict()
for i in msg:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print("the frequency of teh letters are:")
for i in d:
    print("'",i,"'-",d[i])

msg=input("enter teh message")
msg=msg.lower()
d=dict()
for i in msg:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print("the frequency of teh letters are:")                                      #will come for semister exam
for i in d:
    print("'",i,"'- ",'!'*d[i])
'''
'''write a programme that creates 10 key value pairs whrere key is the no in  the range 1 to 10 and the value is twice the no'''
'''msg=[]
for i in range(1,10,2):
    msg.append(i)
d=dict()
for i in msg:
    d[i]=i*2
print(d)
'''
'''functins:'''
''' OOPs-object oriented programming 
-->object 
-->class
-->intragation
-->abstraction
-->inheritance
-->polymorpishm
-->message commucation

'''
''' 
class dog:
    def __init__(self,breed):
        self.breed=breed
mydog=dog("lakshmi")
print(type(mydog.breed))
'''

'''class prog():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def name(self):
        print("hello")
class stud(prog):
    pass
name=stud("k.p","madhavan")
stud.name(stud)
print(name.lname)
'''
'''
write a programme that has a class prog  as inherit from person


class publications:
    def __init__(self,bname,rno,books):
        self.bname=bname
        self.rno=rno
        self.books=books
    def display(self):
        print("book name:",self.bname)
        print("rno:",self.rno)
        print("books",self.books)
class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("gender:",self.gender)
class faculty(person):
    def __init__(self,name,age,gender,bname,rno,books,desing):
        person.__init__(self,name,age,gender)
        self.desing=desing
        self.pub=publications(bname,rno,books)
    def print(self):
        person.display()
        print("desing:",self.desing)
        self.pub.display()
f1=faculty("s.prashanth",17,"male","how to hack me",200,5000,"chief writer")
f1.display()
'''

'''
class rect:
    def __init__(self):
        self.area=0
    def getarea(self,l,b):
        self.area=l*b
        print(self.area)
class circle:
    def __init__(self):
        self.area=0
    def getarea(self,r):
        self.area=r*3.14*r
        print(self.area)
obj1=rect()
obj2=circle()
obj1.getarea(2,3)
obj2.getarea(1)
'''
# ERROR HANDELING .....
'''
try:
    print("hello how are you ")
    a='20'
    b=1
    print(a+b)
    pritn("therer are important errors")
except SyntaxError:
    print("tehere is a syntax error")
except TypeError:
    print("there is an type error")
    print("hey")
finally:
    print("you are wrong ....")
'''
'''
def askint():
    while True:
        try:
            res=int(input("enter teh no"))
        except (TypeError,ValueError):
            print("enter a no not any thing else")
        else:
            print("thankyou you got it right")
            break
        finally:
            print("this is from finally block of code")
askint()

'''
'''importing a module'''
'''
import add2 as a
i=int(input("enter nos"))
j=int(input("enter nos"))
print(a.add(i,j))
if a.ifpos(i):
    print(i," is positive")
else:
    print(i," is negative")
b=int(input("enter the year to find wether it is leap year or not"))
if a.isleapyear(b):
    print("leap year")
else:
    print("nat leap year")
'''
'''
for i in range(6):
    for j in range(i):
        print(j+1,end=")(")
    print()
'''
'''
a=input("enter the no")
list1=[]
ch='y'
while ch=='y' or ch=='Y':
    a = input("enter the no")
    if int(a)>100:
        list1.append("excess")
    else:
        list1.append(a)
    ch=input("enter y to continue")
for i in list1:
    print(i)
'''
class noneg(Exception):
    def disp(self):
        print("the number is negative")
