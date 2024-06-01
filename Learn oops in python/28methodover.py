'''class Calci:
    def add(self, num1=None, num2=None, num3=None):
        if num1 != None and num2 != None and num3 != None:
            print("Addition is:", num1 + num2 + num3)
        elif num1 != None and num2 != None:
            print("Addition is:", num1 + num2)    
        else:
            print("incorrect parameters provided")    

c1 = Calci()
c1.add(10,20)
c1.add(10,20,30)'''

class Area:
    def area(self, l = 0, b = 0):
        if l>0 and b>0:
            print("area of rectangle:", l*b)

        elif l>0 and b == 0:
            print("area of square is:", l*l)    

a = Area()            
a.area(10)
a.area(10,20)


