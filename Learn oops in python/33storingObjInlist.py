class Movie(object):
    def __init__ (self,title,mins,hero):
        self.title = title
        self.runtime = mins
        self.hero = hero
        
    def printer(self):
        print(f"Title is : {self.title}\nruntime is : {self.runtime}\nhero is: {self.hero}")    
list_of_movies = []
while True:
    title = input("Enter the title of movie:")
    mins = input("Enter the runtime of movie:")
    hero = input("Enter the name of hero of movie:")
    obj = Movie(title,mins,hero)
    list_of_movies.append(obj)
    print("Movie added into the list")
    ans = input("Do you want to add another movie(y/n)")
    if ans!= 'y':
        break
    
 
print("All movies information:")
for obj in list_of_movies:
    obj.printer()
    
    

            
