class hello:
    def __init__(self,name,name1):
        self.__name=name
        self.name1=name1
    def disp(self):
        print("from class",self.__name,self.name1)
ob=hello("stv","madu")
ob.disp()
print("from ob",ob.name1)
dict={x:x**2 for x in range(int(input())) if x<10}
print(dict)

