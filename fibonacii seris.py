b=0
j=0
i=0
while i<5:
    if i==1:
        b=1
    sum=j+b
    b=j
    j=sum
    print(j)
    i+=1