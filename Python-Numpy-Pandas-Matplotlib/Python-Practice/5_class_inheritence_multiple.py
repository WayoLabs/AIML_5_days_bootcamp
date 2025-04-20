class Human:
    def __init__(self, name):
        self.name = name

    def speaks(self):
        print(f"{self.name} says, 'How are you?'")

class Actor(Human):
    def do_work(self):
        print(f"{self.name} shoots a film.")

class TennisPlayer(Human):
    def do_work(self):
        print(f"{self.name} plays tennis.")

# Creating objects
tom = Actor("Tom Cruise")
tom.do_work()
tom.speaks()

maria = TennisPlayer("Maria Sharapova")
maria.do_work()
maria.speaks()

print(issubclass(TennisPlayer,Human))
print(issubclass(Human,Actor))




#multiple inheritance
class Father:
    def skills(self):
        print("Father's skills: gardening, programming")

class Mother:
    def skills(self):
        print("Mother's skills: cooking, art")

class Child(Father, Mother):
    def skills(self):
        print("Child inherits:")
        Father.skills(self)
        Mother.skills(self)
        print("Child's own skill: sports")

# Creating an object of Child
c = Child()
c.skills()






def process_file():
   try:
       f=open("data.txt")
       x=1/0
   except FileNotFoundError as e:
       print("inside except")
   finally:
       print("cleaning up file")
       
process_file()









class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll(self, course_name):
        self.courses.append(course_name)
        print(f"{self.name} enrolled in {course_name}")

    def show_courses(self):
        print(f"{self.name}'s Courses: {', '.join(self.courses)}")

# Create list of students
students = [
    Student("Alice", 20, "S001"),
    Student("Bob", 21, "S002")
]

# Enroll students into courses
students[0].enroll("Math")
students[0].enroll("Physics")
students[1].enroll("Biology")

# Display student info and courses
for student in students:
    student.show_info()
    student.show_courses()
    print("-" * 30)











