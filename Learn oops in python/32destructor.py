class  Employee:
    def __init__(self, nm, sal):
        self.name = nm
        self.salary = sal
        
    def display(self):
        print(f"name is {self.name}\nsalary is:{self.salary}")    
        
    #defining destructor    
    def __del__ (self):
        print("Destructor is called")
        
e1 = Employee("Berlin", 5000)        
e1.display()