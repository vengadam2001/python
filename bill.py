print("**********BILLING SYSYTEM**********")
a={"milk":30,"ghee":40,"milkshake":25,"ice cream":40}
#b=[30,40,25,15]
totalamount=0
amount=0
while True:
    print("1.milk\n2.ghee\n3.milkshake\n4.ice cream")
    item=input("Enter the item:")
    for i in a:
       # print(a[i])
        if(item==i):
            amount=a[i]
            print(i,"=",a[i])
    totalamount+=amount
    print("Do you want to continue(y/n):")
    ch=input()
    if(ch=='n' or ch=='N'):
        break
print("Total amount:",totalamount)
if(totalamount>=300):
    print("Discount Amount+_=",(totalamount*5)/100)
    totalamount+=(totalamount*5)/100
print("GST=2.5% & TAX=1%")
print("Net amount=",totalamount+(3.5*totalamount)/100)

