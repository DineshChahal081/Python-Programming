''''class Computer(object):
    def __init__(self):
        self.ram='8gb' 
        self.storage='512gb'
        print("computer class constructor")
class Mobile(Computer):
    def __init__(self):
        super().__init__()
        self.model='iphone x'
        print("mobile class constructor called")

Apple=Mobile()
print(Apple.__dict__)'''

'''class Computer(object):
    def __init__(self, ram, storage):
        self.ram=ram
        self.storage=storage
        print("computer class constructor")
class Mobile(Computer):
    def __init__(self):
        super().__init__('8gb','512gb')
        self.model='iphone x'
        print("mobile class constructor called")

Apple=Mobile()
print(Apple.__dict__)'''


class Computer(object):
    def __init__(self, ram, storage):
        self.ram=ram
        self.storage=storage
        print("computer class constructor")
class Mobile(Computer):
    def __init__(self,ram,storage):
        super().__init__(ram,storage)
        self.model='iphone x'
        print("mobile class constructor called")

Apple=Mobile('8gb','512gb')
print(Apple.__dict__)
