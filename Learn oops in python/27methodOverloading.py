class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages
        
    def __add__(self, other): #(b1,b2)    
        total = self.pages + other.pages
        return Book('All books', total)

    def __str__(self):
        return str(self.pages)    
    
    
b1 = Book('one indian girl', 300)    
b2 = Book('making india awesome', 200)
b3 = Book('half girlfriend', 400)


print("total number of pages:", b1 + b2 + b3) #b1.__add__(b2) --Book.__add__(b1,b2)
    