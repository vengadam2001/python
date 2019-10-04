s=input()
d=dict()
z=0
for i in s:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
k=0
for i in d:
  if k==0:
    z=i
    k=2
  if d[i]>d[z]:
    z=i
k=0
print(z,d[z])
d.pop(z)
k=0
for i in d:
  if k==0:
    z=i
    k=2
  if d[i]>d[z]:
    z=i
k=0
print(z,d[z])
d.pop(z)
k=0
for i in d:
  if k==0:
    z=i
    k=2
  if d[i]>d[z]:
    z=i
k=0
print(z,d[z])
d.pop(z)
