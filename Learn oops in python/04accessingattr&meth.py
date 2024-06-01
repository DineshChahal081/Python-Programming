class Employee:
    def __init__(self, sal, ag):
        self.salary=sal
        self.age=ag
        
    def display(self):
        print(f"Salary is {self.salary} and age is {self.age}")   
        
e1=Employee(20000,21)
e2=Employee(25000,23)

#accessing atrribute outside the class
e1.salary
#print(e1.salary)

#updating attribute
e1.salary=22000
print(e1.salary)

#accessing method outside the class
e2.display() 