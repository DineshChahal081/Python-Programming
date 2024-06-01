class Decorator(object):
    def __init__(self,func):
        self.function = func
    
    def __call__(self,a,b):
         result = self.function(a,b)
         return result**2
    
@Decorator    
def add(a, b):
    return a+b

    
print(add(1,2))