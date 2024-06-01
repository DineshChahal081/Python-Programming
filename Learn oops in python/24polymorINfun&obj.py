class BMW:
    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        print("max speed is 200")    

class Ferrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("max speed is 180")    
        
def car_details(obj):
    obj.fuel_type()
    obj.max_speed()
    
bmw =BMW()
ferrari = Ferrari()

car_details(bmw)  
print("----------")
car_details(ferrari)

        