class Employee:
    company_name="infosys" #class variable
    def __init__(self, nm, sal):
        self.name=nm
        self.salary=sal
        
      
    @classmethod #decorator
    def get_company_name(cls):
        print(f"company is:", cls.company_name )
    
e1=Employee("Ashu", 53000)
e2=Employee("Amit", 50000)

Employee.get_company_name()
print(Employee.company_name)#infosys

#accessing using object reference
print(e1.company_name) #infosys


#modification using class reference
Employee.company_name='tcs'
print(Employee.company_name) 


