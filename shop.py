sname = ["saravana stores", "T-Nagar chennai"]
qty = []
dis = []
tax = []
prod = []
mrp = []
sno=[0]

def enter():
    ch = 'y'
    n=sno.pop()
    sno.append(n)
    while ch == 'y' or ch == 'Y':
        prod.append(input("enter the product name:"))
        qty.append(int(input("enter the qty of product:")))
        mrp.append(float(input("enter the price")))
        dis.append(float(input("enter the discount")))
        tax.append(float(input("enter the tax in percentage")))
        sno.append(n)
        ch = input("do you want to continue(Y/N):")
        n+=1

def sales():
    ch = 'y'
    b = []
    q = []
    j = 0
    sum = 0
    while ch == 'y' or ch == 'Y':
        print("sno\titem\tqty\tprice\ttax")
        for i in sno:
            print(i, '\t', prod[i], '\t', qty[i], '\t', mrp[i] - (mrp[i] * dis[i] / 100), '\t',(mrp[i] * tax[i] / 100))
        b.append(int(input("enter the serial no of the product:")))
        q.append(int(input("enter the quantity of the product")))
        j += 1
        ch=input("do you want to continue(y/n)")
    print("the bill is:")
    print(f"\n\n\t\t{sname[0]}\n\t\t{sname[1]}")
    print("sno\titem\tqty\tprice\ttax")

    for i in range(0, j, 1):
        qty[b[i]] -= q[i]
        sum += ( mrp[b[i]] * q[i] ) - (dis[b[i]] * mrp[b[i]]/100) + (tax[b[i]]*mrp[b[i]]/100)
        print(f"\n{i + 1}\t{prod[b[i]]}\t{q[i]}\t{mrp[b[i]] * q[i]}\t{q[i] * tax[b[i]]}")
    print(f"\ntotal is:{sum}")
while True:
    print("\n enter 1 to buy\n enter 2 to sell\nenter 0 to exit")
    c=int(input(""))
    if c==1:
        enter()
    elif c==2:
        sales()
    elif c==0:
        exit(0)
    else:
        print("enter the correct option")