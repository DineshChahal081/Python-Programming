class Country:
    def __init__(self):
        print("Country class constructor")
        self.office='Delhi'

class State:
    def __init__(self):
        print("State class constructor")
        self.office='Chandigarh'
        
class District(State,Country):
    def __init__(self):
        super().__init__()
        print("District class constructor")
        self.office='Jind'

d=District()        
print(d.office)
print(d.__dict__)           