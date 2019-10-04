def print_rangoli(size):
    # your code goes here
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    n=size-1
#for the top part
    for i in range(size):
        print("--"*(n-i),end="")
        #for the left upper part
        for j in range(i+1):
            print(letters[n-j]+"-",end="")
        #for the right lower part
        a=i
        a+=n-i
        for j in range(n-i,a):
            print(letters[j+1],end="")
            if i == n and j==a-1:
                pass
            else:
                print("-",end="")
        print("-"*(((n-i)*2)-1))
#for the bottom part
    #for the bottom left part
    for i in range(1,size):
        print("--"*i,end="")
        #for the bottom right part
        for j in range(n-i+1):
            print(letters[n-j],end="")
            if i == size-1 :
                pass
            else:
                print("-",end="")
        
        for j in range(n-i):
            print(letters[i+j+1],end="")
            a+=1
            if j == size-i:
                pass
            else:
                print("-",end="")
        print("--"*i)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
