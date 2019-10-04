def pos(list1,filename):
    with open("text.txt","w") as f:
        count=0
        for i in list1:
            if i>-1:
                count+=1
        f.write(str(count))

