n=int(input())
l=[]
for i in range(n):
  l.append(input())
d=dict()
for i in l:
    if i in d:
      d[i]+=1
    else:
      d[i]=1
print(len(d))
for i in d:
  print(d[i],end=" ")
      
