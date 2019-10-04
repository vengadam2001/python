x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[1,2,3],[4,5,6],[7,8,9]]
res=[]
for i in range(0,len(x),1):
    res.append([])
    for j in range(0,len(x[0]),1):
        res[i].append(x[i][j]+y[i][j])
for i in range(0,len(x)):
    print(res[i])