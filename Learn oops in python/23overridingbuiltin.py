'''class Cart:
    def __str__(self):
        return "This is class Cart object"

c1 =Cart()
print(c1)'''  

class Cart:
    def __init__ (self, basket1, basket2, basket3):
        self.clothes = basket1
        self.electronics = basket2
        self.other = basket3
        
    def __len__ (self):
        print("total number of items in cart:")     
        return len(self.clothes) + len(self.electronics) + len(self.other)

shantanu = Cart(['pant', 'shirt', 't-shirt'], ['earphone','mobile'], ['chair'])        
print(len(shantanu))
