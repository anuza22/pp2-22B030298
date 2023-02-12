class Shape:
    length =0

    def __init__ (self, length):
        self.length = length

    def area(self):
        # print( self.length**2)
        print(self.length * self.length == 0)  
      

class Square(Shape):
    def area(self):
        print( self.length**2)

x1 = Shape()
x1.area()
