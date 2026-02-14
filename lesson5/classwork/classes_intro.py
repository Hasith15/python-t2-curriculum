# class is a blueprint for making objects
# each object can store data and do actions
class Student:
    # __init__ is the constructor. it runs automatically when you create a Student()
    # "self" means "this specific object" the student you're creating
    def __init__(self, name, grade): # save the students name and grade as attributes on this object
        self.name = name
        self.grade = grade
                                                                           
    def introduce(self): # A method is a function that belongs to the class
        print("Hi my name is", self.name)
        print("I am in grade", self.grade)

student1 = Student("Max", 11)
student1.introduce()

student2 = Student("Ben", 10)
student2.introduce()

student2.grade = 12
student2.introduce()

student2.name = "Benjamin"
student1.introduce()