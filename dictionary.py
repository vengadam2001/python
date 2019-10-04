                                                #dictinory
d={1:[],2:[],3:[]}
d[1].append("hello man")
d[1].append("omg")
d[2].append("hey you ")
d[3].append("hi da")
print(d)
'''write a programme that has a set of words in english words and corresponding words in hindi'''
'''define another dict that has alist of words in hindi and the corresponding words in urudu'''
'''take all words from english lang and 
display their meanings in both the lang '''
'''
d={"regno":1234,"name":"thiru","mobile":12345678}
print(d)
'''
'''
eh={"friend":"dhosth","food":"kana","book":"kithab"}
ht={"dhosth":"shahithu","kana":"haharam","kithab":"gratham"}
for i in eh:
    print(i,"in hindi is",eh[i],"in telagu is",ht[eh[i]])
'''
'''write a python programme to print the frequency of character occuring in a message'''
'''
msg=input("enter teh message")
msg=msg.lower()
d=dict()
for i in msg:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print("the frequency of teh letters are:")
for i in d:
    print("'",i,"'-",d[i])

msg=input("enter teh message")
msg=msg.lower()
d=dict()
for i in msg:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print("the frequency of teh letters are:")                                      #will come for semister exam
for i in d:
    print("'",i,"'- ",'!'*d[i])
'''
'''write a programme that creates 10 key value pairs whrere key is the no in  the range 1 to 10 and the value is twice the no'''
msg=[]
for i in range(1,10,2):
    msg.append(i)
d=dict()
for i in msg:
    d[i]=i*2
print(d)