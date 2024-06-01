class Student:
    def __init__(self, nm, m):
        self.name=nm
        self.marks=m
        
    def display(self):
        print(self.name, self.marks)   

    def change_data(self):
        self.name=input("enter new name: ")
        self.marks=int(input("enter new marks: "))


std1 = Student('Amit', 89)        
std2 = Student('Ashu', 90) 
std3 = Student('Hitesh', 85) 

#instance method
std1.display()

#outside the class
std2.change_data()
print(std2.__dict__)