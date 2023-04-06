class Human:
    def __init__(self, gender):
        self.gender = gender
    
    def printInfo(self):
        print(self.gender)
#gender = m/f
#printInfo(gender)
class Person(Human):
    def __init__(self, name, nationality, gender):
        self.name = name
        self.nationality = nationality
        Human.__init__(self, gender)
    

    def printInfo(self):
        print(self.name, self.nationality)

    def setSurname(self, surname):
        self.surname = surname
    
    def getSurname(self):
        print(self.surname)

class Student(Person):
    def __init__(self, name, nationality, id, gender):
        self.id = id
        Person.__init__(self, name, nationality, gender)
    
    
    def printInfo(self):
        print(self.name, self.nationality, self.id, self.gender)

    def setSurname(self, surname):
        self.surname = surname
    
    def getSurname(self):
        print(self.surname)

class Teacher(Person):
    def __init__(self, name, nationality, teacherId, gender):
        self.teacherId = teacherId
        Person.__init__(self, name, nationality, gender)

    def printInfo(self):
        print(self.name, self.nationality, self.teacherId, self.gender)

    def setSurname(self, surname):
        self.surname = surname
    
    def getSurname(self):
        print(self.surname)

k = Human("f")
k.printInfo()
obj = Person("Anuza", "kazakh", "f")
obj.printInfo()
obj.setSurname("Akturina")
obj.getSurname()

obj1 = Student("Anuza", "kazakh", 74545364, 'f')
obj1.printInfo()
obj1.setSurname("Akturina")
obj1.getSurname()


obj2 = Teacher("Arnur", "kazakh", 4783874563874, "m")
obj2.printInfo()
obj1.setSurname("Kelgenbaev")
obj1.getSurname()

    
    
