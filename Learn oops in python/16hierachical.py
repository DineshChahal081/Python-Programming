class Person:
    def __init__(self, nm, ag):
        self.name = nm
        self.age = ag
    def display1(self):
        print("This is person display")    
    
class Employee(Person):
    def __init__(self, nm, ag, sal):
        super().__init__(nm, ag)  
        self.salary = sal
    def display2(self):
        print("This is Employee display") 
               
class Student(Person):
    def __init__(self, nm, ag, m):
        super().__init__(nm, ag)
        self.marks = m
    def display3(self):
        print("This is student display")   
         
s1 = Student('jay', 21, 90) 
e1 = Employee('Ashu', 23, 40000)
p1 = Person('Kapil', 20)

print(s1.__dict__)
print(e1.__dict__)
print(p1.__dict__)

s1.display3()
s1.display1()
