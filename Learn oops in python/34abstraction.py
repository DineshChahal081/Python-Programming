from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
    def color(self):
        print("white")
        
class Maruti_Suzuki(Car):
    def mileage(self):
        print("mileage is 30kmph")  
        

class TATA(Car):
    def mileage(self):
        print("mileage is 35kmph")   


class Duster(Car):
    def mileage(self):
        print("mileage is 40kmph")                   
              
c1 = Car()
m1 = Maruti_Suzuki()    
t1 = TATA()
d1 = Duster()
m1.mileage()
t1.mileage()