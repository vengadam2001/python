s=input().split()
m=int(s[1])
n=int(s[0])

#for the top part
for i in range(n//2):
    a=(n//2)-i
    for j in range(a):
        print("---",end="")
    for j in range(n-(2*a)):
        print(".|.",end="")
    for j in range(a):
        print("---",end="")
    print()
#for the welcome line
a=(n//2)-1
print("---"*a,end="")
print("-WELCOME-",end="")
print("---"*a,end="")   
print()
#for the bottom line
for i in range(n//2):
    a=i+1
    for j in range(a):
        print("---",end="")
    for j in range(n-(2*a)):
        print(".|.",end="")
    for j in range(a):
        print("---",end="")
    print()
