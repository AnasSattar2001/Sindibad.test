# Management System
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to {self.course_name}.")

    def list_students(self):
        for student in self.students:
            print(student.name)

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}

    def enroll(self, course):
        if course.course_name not in self.courses:
            self.courses[course.course_name] = None
            course.add_student(self)
        else:
            print(f"Already enrolled in {course.course_name}.")

    def set_grade(self, course, grade):
        if course.course_name in self.courses:
            self.courses[course.course_name] = grade
        else:
            print(f"{self.name} is not enrolled in {course.course_name}.")

    def get_grades(self):
        return self.courses

class Instructor:
    def __init__(self, name, instructor_id):
        self.name = name
        self.instructor_id = instructor_id

    def assign_grade(self, student, course, grade):
        student.set_grade(course, grade)
        print(f"Grade {grade} assigned to {student.name} for {course.course_name}.")

# Management System
course_math = Course("Math 101")
student1 = Student("John Doe", "S001")
instructor1 = Instructor("Dr. Smith", "I001")

student1.enroll(course_math)
instructor1.assign_grade(student1, course_math, 95)

print(f"Grades for {student1.name}: {student1.get_grades()}")
