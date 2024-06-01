class Employee:
    def __init__(self, nm, ag):
        self.name=nm
        self.age=ag
        
e1=Employee('Amit', 22)
e2=Employee('AShu', 21)

print(getattr(e1,'age'))

setattr(e2,'name','Berlin')        
print(e2.__dict__)

delattr(e2,'age')
print(e2.__dict__)

print(hasattr(e1,'name'))
print(hasattr(e1,'nam'))