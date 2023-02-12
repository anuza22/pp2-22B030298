class Person:
    def __init__ (self):
        self.fname = ''
    def getstring(self):
        self.fname = input()

    def printString(self):
        print(self.fname.upper())

s = Person()
s.getstring()
s.printString()

