
class Student:
    def __init__(self, name, age):
        self.name = name      
        self.age = age        

    def intro(self):      
        print("My name is", self.name, "and I am", self.age, "years old.")


s1 = Student("Silvester", 24)
s2 = Student("Silva", 24)


s1.intro()
s2.intro()