import re
try:
    s=input("enter eth email")
    l=s.split('@')
    a=l[1].split('.')
    l.pop()
    l.append(a[0])
    l.append(a[1])
    print(l)
    if re.search('@',s) or re.search('.',s):
        if len(l)==3 and len(l[2])<=3 and (re.search('[a-z]',l[0]) or re.search('[A-Z]',l[0])or re.search('[_-]',l[0])):
            print(True)
except IndexError:
    print(False)