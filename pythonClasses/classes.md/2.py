class Shape:
    length =0

    def __init__ (self, length):
        self.length = length

    def area(self):
        print( self.length**2)
      

class Square(Shape):
    def area(self):
        print( self.length**2)

x1 = Square(5)
x1.area()
