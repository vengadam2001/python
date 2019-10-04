def minion_game(string):
    # your code goes here
    s=0
    k=0
    vList=[]
    cList=[]
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            a=string[i:j]
            if a[0] in "AEIOUaeiou":
                vList.append(a)
                k+=1
            else:
                cList.append(a)
                s+=1
    if len(cList)>len(vList):
        print("Sturat",s)
    else:
        print("Kevin",k)


if __name__ == '__main__':
    s = input()
    minion_game(s)
