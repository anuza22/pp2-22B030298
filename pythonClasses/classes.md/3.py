class Shape:
    lenght =0
    def __init__ (self, lenght):
        self.lenght = lenght

    def area(self, lenght):
       print(lenght**2)

class Square(Shape):
    def area(self):
        print( self.lenght**2)

class Rectangle(Shape):
    def __init__ (self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        print( self.lenght*self.width)



x1 = Rectangle(5, 2)
x1.area()


