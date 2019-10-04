'''def pigname(word1="pig"):
    firstletter=word1[0]
    if firstletter in  "aeiou":
        pig=word1+"hero"
    else:
        pig=word1[1:]+firstletter+'ay'
    return(pig)
wor=input("enter the name")
print(pigname(wor))
'''
'''
def defaultarg(course="python"):
    if not course:
        print("python")
    else:
        print(course)
name=input("enter your name")
course=input("enter your course:")
defaultarg(course)
'''
'''
def subtract(*args):
    res=2*args[0]
    for i in args:
        res-=i
    return(res)
def addition(*args):
    return(sum(args))
def mul(*args):
    res=1
    for i in args:
        res*=i
    return(res)
def div(*args):
    res=args[0]**2
    for i in args:
        res/=i
    return(res)
def area(*args):
    return(mul(args[0],args[1]))
def si(p,n,r):
    return(p*n*r/100)
a=int(input("enter the no"))
b =int(input("enter the no"))
print(subtract(a,b))
print(addition(a,b))
print(mul(a,b))
print(div(a,b))
print(area(a,b))
print(si(a,b))
'''
'''
def even_odd(a):
    if a%2==0:
        return(True)
a=int(input("enter the number"))
if even_odd(a):
    print("even")
else:
    print("odd")
'''
'''
def check(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            return(a)
        else:
            return(b)
    else:
        if a>b:
            return(a)
        else:
            return(b)
a=int(input("enter the no"))
b=int(input("enter the no"))
print(check(a,b))
'''
'''
def check(s):
    f=s.lower().split()
    return(f[0][0]==f[1][0])
print(check(input("enter the string")))
'''
'''
hi=open("text.txt",'w')
hi.write("hello")
hi.close()

hello=open("text.txt",'r')
if hello:
    hello.seek(0)
    line=hello.read()
    print(line)
else:
    print("file not found")
hello.close()
'''

'''
list1=input("enter the word")
with open("text1.txt",'w') as fout:
    print(fout.write(list1))
scount=0
ncount=0
tcount=0
fout.close()
with open("text1.txt",'r') as fin:
    list1=fin.read()
    for i in list1:
        if i==' ':
            scount+=1
        elif i=='\t':
            tcount+=1
        elif i=='\n':
            ncount+=1
print("no of space is:",scount)
print("no of tab is:",tcount)
print("no of new line:",ncount)
fin.close()
'''

'''a=input("enter the file name")
b=input("enter the file name")
with open(b,'r') as fin:
    with open(a,'w') as fout:
        text=fin.read()
        fout.write(text)
        fout.close()
    fin.close()
'''
''''''
'''b=input("enter the file name")
word=input("enter the word to be searched")
k=0
with open(b,"r") as fin:
    for line in fin:
        text=line.split()
        for i in text:
            if i==word:
                k+=1
print("the ",word," occurs ",k,"times")'''

'''import re
b=input("enter the file name")
k=0
with open(b,"r") as fin:
    line=fin.read()
    w=re.findall("\w",line)
    for i in w:
        k+=1
print("occurs ",k,"times")'''
'''
import pickle
list1=1
a=open("text.dat","ab")
pickle.dump(list1,a)
lon=0
a.close()
a=open("text.dat","rb")
for i in range(10):
    lon=pickle.load(a)
    print(lon)
a.close()
'''
'''
a=open("text.txt",mode='a')
print(a.write("hello ."))
a.close()
a=open("text.txt",mode='r')
print(a.read())
a.close()'''
'''
vcount=0
ccount=0
ocount=0
with open("text.txt",'r') as a:
    para=a.read()
    for ch in para:
        if ch in "aeiouAEIOU":
            vcount+=1
        elif ch.isalpha():
            ccount+=1
        else:
            ocount+=1
    print("the percentage of vowels is:",(vcount/(vcount+ccount+ocount))*100,"%")
    print("the percentage of consonants is:", (ccount / (vcount + ccount + ocount)) * 100,"%")
    print("the percentage of other characters is:", (ocount / (vcount + ccount + ocount)) * 100,"%")
    print("total percent is:",((vcount/(vcount+ccount+ocount))*100)+((ccount/(ccount+vcount+ocount))*100)+((ocount/(vcount+ccount+ocount))*100),"%")
'''
#WRITE A PROG TO GENDRATE A QUIZ AND USE 2 FILES question.txt and answer.txt the programme opens question.txt and read teh question with option on the screen
'''
q=open("text.txt",'r')
a=open("text1.txt",'r')
for i in q.read():
    print(i)
ans=input("enter the correct option")
'''
import pickle
f=open()