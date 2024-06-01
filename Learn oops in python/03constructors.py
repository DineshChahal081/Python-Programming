#non-parameterized constructor
'''class Employee:
    def __init__(self):
        self.salary=22000
        self.age=21
        
e1=Employee()
e2=Employee()
print(e1.__dict__)''' 

     
#parameterized constructor
''''class Employee:
    def __init__(self, sal, ag):
        self.salary=sal
        self.age=ag
        
e1=Employee(20000,21)
e2=Employee(25000,23)
print(e1.__dict__)        
print(e2.__dict__)'''

#default constructor
class Employee:
    pass

e1=Employee()
e2=Employee()
print(e1.__dict__)