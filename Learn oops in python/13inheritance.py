#constructor over-riding in inheritance

'''class Father:
    def __init__(self):
        print("father constructor called")
        self.vehicle="scooter"
      
      
class Son(Father):
    pass  

s=Son()        
print(s.__dict__)'''

class Father:
    def __init__(self):
        print("father constructor called")
        self.vehicle="scooter"
      
      
class Son(Father):
     def __init__(self):
        print("son  constructor called")
        self.vehicle="Car"

s=Son()        
print(s.__dict__)
        
        