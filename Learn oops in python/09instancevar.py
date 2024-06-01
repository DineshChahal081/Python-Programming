class Student:
    def __init__(self, nm, m):
        self.name=nm
        self.marks=m
        
std1 = Student('Amit', 89)        
std2 = Student('Ashu', 90) 
std3 = Student('Hitesh', 85) 

#instance variable...outside the class
std1.age=21
del std1.marks #operations
print(std1.__dict__)
print(std2.__dict__)