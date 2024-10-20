import json

class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

    def __str__(self):
        return f"ID: {self.person_id}, Name: {self.name}"

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        self.courses = {}
    
    def enroll(self, course):
        if course.name not in self.courses:
            self.courses[course.name] = None  # Grade not assigned yet
            course.add_student(self)
        else:
            print(f"Student {self.name} is already enrolled in {course.name}.")
    
    def set_grade(self, course, grade):
        if course.name in self.courses:
            self.courses[course.name] = grade
        else:
            print(f"Student {self.name} is not enrolled in {course.name}.")

    def get_grades(self):
        return self.courses

class Instructor(Person):
    def __init__(self, name, instructor_id):
        super().__init__(name, instructor_id)
        self.courses = []
    
    def assign_course(self, course):
        self.courses.append(course)
        course.set_instructor(self)
    
    def grade_student(self, student, course, grade):
        if course in self.courses:
            student.set_grade(course, grade)
        else:
            print(f"{self.name} does not teach {course.name}.")

class Administrator(Person):
    def __init__(self, name, admin_id):
        super().__init__(name, admin_id)
    
    def add_course(self, name):
        return Course(name)
    
    def remove_course(self, course):
        del course
        print(f"Course {course.name} removed.")

class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.instructor = None
    
    def add_student(self, student):
        self.students.append(student)
    
    def set_instructor(self, instructor):
        self.instructor = instructor

# File handling for saving and loading data
class FileHandler:
    @staticmethod
    def save_data(filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file)
    
    @staticmethod
    def load_data(filename):
        with open(filename, 'r') as file:
            return json.load(file)

# Example system simulation
if __name__ == "__main__":
    admin = Administrator("Alice", "001")
    
    # Creating a course
    course_math = admin.add_course("Math 101")
    
    # Creating a student and instructor
    student1 = Student("John Doe", "S001")
    instructor1 = Instructor("Dr. Smith", "I001")
    
    # Assign course to the instructor
    instructor1.assign_course(course_math)
    
    # Enroll the student in the course
    student1.enroll(course_math)
    
    # Instructor grades the student
    instructor1.grade_student(student1, course_math, 90)
    
    # Display grades
    print(f"Grades for {student1.name}: {student1.get_grades()}")
    
    # Saving and loading student data as an example of file handling
    student_data = {"name": student1.name, "ID": student1.person_id, "grades": student1.get_grades()}
    FileHandler.save_data('student_data.json', student_data)
    loaded_data = FileHandler.load_data('student_data.json')
    print(f"Loaded Data: {loaded_data}")
