#
#
#
#
#

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age

        print("{0} is {1} years old.".format(self.name, self.age))

p1 = Person("Kazu", 47)
p2 = Person("Mary", 27)

