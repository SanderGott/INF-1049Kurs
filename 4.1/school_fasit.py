import csv
import os


class Student:
    def __init__(self, studentID, name):
        self.ID = studentID
        self.name = name

        self.grades = {}
    

    def addGrade(self, courseName, grade):
        self.grades[courseName] = grade
    
    def getGrade(self, courseName):
        return self.grades[courseName]

    def getAverageGrade(self):
        total = 0
        for grade in self.grades.values():
            total += grade
        return total / len(self.grades)


class School:
    def __init__(self):
        self.students = {}
    
    def addStudent(self, student):
        self.students[student.ID] = student
    
    def getStudent(self, studentID):
        return self.students[studentID]

    def getAverageGrade(self):
        total = 0
        count = 0
        for student in self.students.values():
            total += student.getAverageGrade()
            count += 1
        return total / count
    
    def getClassAverageGrade(self, courseName):
        total = 0
        count = 0
        for student in self.students.values():
            if courseName in student.grades:
                total += student.grades[courseName]
                count += 1
        if count == 0:
            return 0
        return total / count

    def getCoursesAverageGrade(self):
        courses = {}
        for student in self.students.values():
            for course, grade in student.grades.items():
                if course in courses:
                    courses[course].append(grade)
                else:
                    courses[course] = [grade]

        for course, grades in courses.items():
            courses[course] = sum(grades) / len(grades)
        
        
        return courses
    
    def getStudentGradesUnder2(self):
        l = []
        for student in self.students.values():
            if student.getAverageGrade() < 2:
                l.append((student.ID, student.name))
        
        return l





def import_students_from_csv(school, file_path):
    """
    Import students and their grades from a CSV file into the School instance.

    Parameters:
        school (School): The school instance to populate.
        file_path (str): Path to the CSV file containing student data.
    """
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            student_id = int(row["StudentID"])
            name = row["Name"]
            student = Student(student_id, name)
            
            # Add grades for each course
            for course, grade in row.items():
                if course not in ["StudentID", "Name"]:
                    student.addGrade(course, int(grade))
            
            # Add the student to the school
            school.addStudent(student)


school = School()
import_students_from_csv(school, os.path.join(os.path.dirname(__file__), "students.csv"))

print(f"Total students: {len(school.students)}")
print(f"Average grade in school: {school.getAverageGrade():.2f}")
print("Course average grades:")
for course, avg_grade in school.getCoursesAverageGrade().items():
    print(f"  {course}: {avg_grade:.2f}")

print("Students with average grade under 2:")
for student_id, name in school.getStudentGradesUnder2():
    print(f"  {student_id}: {name}")
