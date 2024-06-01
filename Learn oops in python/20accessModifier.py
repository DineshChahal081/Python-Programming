#public
'''class Finance:
    def __init__(self):
        self.revenue = 1000000
        self.number_of_sales = 114
        
        
f1 = Finance()
print(f1.__dict__)

class HR:
    def __init__(self):
        self.number_of_emp = 32
        f1.revenue = 1
        
h1 = HR()        
print(f1.__dict__)'''


''''revenue': 1000000, 'number_of_sales': 114}
{'revenue': 1, 'number_of_sales': 114}'''
#bina encapsulation kiye Hr class Finance class ko modify kr skti
#hai ye...nhi hona chahiye iske liye encapsulation krte hai


class Finance:
    def __init__(self):
        self.__revenue = 1000000 #private data
        
        self._number_of_sales = 114 #protected data
        
        
f1 = Finance()
print(f1.__dict__)

class HR:
    def __init__(self):
        self.number_of_emp = 32
        f1.__revenue = 1
        
h1 = HR()        
print(f1.__dict__)