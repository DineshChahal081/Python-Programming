class Veh:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        
    def get_details(self):
        print("name is:", self.name)    
        print("color is:", self.color)
        print("price is:", self.price)
        
    def max_speed(self):
        print("maixmum speed limit is 100")    

    def gear(self):
        print("gear change is 6")   
        
class Car(Veh):
    def max_speed(self):
       print("maixmum speed limit is 140")    

    def gear(self):
       print("gear change is 7")   
                   
v1 = Veh("Truck", 'red', 2000000)                   
c1 = Car("Car",'white', 5000000)
v1.get_details()
c1.get_details()

v1.max_speed()
c1.max_speed()


