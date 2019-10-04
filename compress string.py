s=input()
l=[]
cnt=0
List=[]
for i in range(len(s)):
    if len(s)>i+1:
        if s[i]==s[i+1]:
            cnt+=1
        else:
            cnt+=1
            l.append(s[i])
            l.append(cnt)
            cnt=0
else:
    cnt+=1
    l.append(s[i])
    l.append(cnt)
    cnt=0
print(l)
for i in range(0,len(l),2):
    List=[l[i],l[i+1]]
    t=tuple(List)
    print(
