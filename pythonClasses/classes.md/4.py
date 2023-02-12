import math
class Point:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2

    def move(self):
        self.d1, self.d2 = map(int,  input().split())
        

    def show(self):
        print(self.d1, self.d2)

    def dist(self, x, y):
        bet = math.sqrt((self.d1-x)**2 + (self.d2-y)**2)
        print(bet)

c = Point(5, 3)
c.show()
c.move()
c.show()
c.dist(2, 2)

