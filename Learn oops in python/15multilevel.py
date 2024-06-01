#constructor in multilevel inheritance

'''class Human_being(object):
    def __init__(self):
        print("human being constructor called")
        self.name=input("Enter your name")
        
class Employee(Human_being):
    def __init__(self):
        print("employee constructor called")
        self.salary=input("Enter your salary")        

class Managers(Employee):
    def __init__(self):
        print("managers constructor called")
        self.bonus=float(input("Enter your bonus") )       

#m1=Managers() 
e1=Employee()'''

#constructor in multilevel inheritance

'''class Human_being(object):
    def __init__(self):
        print("human being constructor called")
        self.name=input("Enter your name")
        
class Employee(Human_being):
    def __init__(self):
        print("employee constructor called")
        self.salary=input("Enter your salary")        

class Managers(Employee):
    pass    

m1=Managers()'''


#variables in multilevel
class Human_being(object):
      salary=10000
class Employee(Human_being):  
       salary=20000  
class Managers(Employee):  
        salary=50000
        
m1=Managers()          
print(m1.salary)