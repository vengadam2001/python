def add(a,b):
    return(a+b)
def ifpos(a):
    if a>=0:
        return(True)
    else:
        return(False)
def isleapyear(a):
    if a%4==0 and a%100!=0:
        return(True)
    else:
        return(False)