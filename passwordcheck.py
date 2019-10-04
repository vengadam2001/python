import re
val=[]
alphabet=0
ALPHABET=0
number=0

a=input("enter the password")
b=re.findall(r'\w',a)
if len(b)>6 and len(b)<12:
    for i in b:
        if re.search("[a-z]",i):
            alphabet=10
        else:
            print("wrong1")
        if re.search("[A-Z]",i):
            ALPHABET=10
        else:
            print("wrong2")
        if re.search("[0-9]",i):
            number=10
        else:
            print("wrong3")
        print(alphabet,ALPHABET,number)
    if alphabet==10 and ALPHABET==10 and number==10:
        print("true password")
    else:
        print("naot eligible")
else:
    print("not elegible")