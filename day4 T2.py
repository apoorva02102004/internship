# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def display_person(self):
        print("Name:", self.name)


# Student class
class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def display_student(self):
        self.display_person()
        print("Student ID:", self.student_id)


# SportsPlayer class
class SportsPlayer(Person):
    def __init__(self, name, sport_name):
        super().__init__(name)
        self.sport_name = sport_name

    def display_sports_player(self):
        self.display_person()
        print("Sport:", self.sport_name)


# CollegeStudent class (Hybrid Inheritance)
class CollegeStudent(Student, SportsPlayer):
    def __init__(self, name, student_id, sport_name, college_name):
        super().__init__(name, student_id)
        self.sport_name = sport_name
        self.college_name = college_name

    def display_college_student(self):
        print("College Name:", self.college_name)
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Sport:", self.sport_name)


# Create object
college_student = CollegeStudent(
    name="Rahul",
    student_id="STU101",
    sport_name="Cricket",
    college_name="ABC Engineering College"
)

# Display all details
college_student.display_college_student()
