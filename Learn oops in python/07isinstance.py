class demo:
    pass
d1=demo()

class Employee:
    def __init__(self, sal, ag):
        self.salary=sal
        self.age=ag
        
e1=Employee(20000,21)
e2=Employee(25000,23)

print(isinstance(e1,Employee))
print(isinstance(d1,Employee))
print(isinstance(d1,demo))