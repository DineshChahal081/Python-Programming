class Outer:
    def __init__(self):
        print("outer class constructor called")

    def display(self):
        print("This is display method")    

    class Inner:
        def __init__(self):
            print("inner constructuon called")   
        def show(self):
            print("This is show method")    

obj = Outer()
in1 = obj.Inner()
in1.show()
obj.display()
            