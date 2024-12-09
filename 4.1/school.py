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
        """
        Returnerer snittkarakter for studenten
        """


class School:
    def __init__(self):
        self.students = {}
    
    def addStudent(self, student):
        self.students[student.ID] = student
    
    def getStudent(self, studentID):
        return self.students[studentID]

    def getAverageGrade(self):
        """
        Returnerer snittkarakter for hele skolen
        """
    
    def getClassAverageGrade(self, courseName):
        """
        Returnerer gjennomsnittskarakteren for et emne
        """

    def getCoursesAverageGrade(self):
        """
        Returnerer en dictionary med gjennomsnittskarakteren for hvert emne.

        {
        "Math": 3.2,
        "Science": 2.7, etc...
        }
        """
    
    def getStudentGradesUnder2(self):
        """
        Returner en liste med studenter med snittkarakter under 2. 
        På format: [(student_id, student_name), ...]
        """





def import_students_from_csv(school, file_path):
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            student_id = int(row["StudentID"])
            name = row["Name"]
            student = Student(student_id, name)
            
            for course, grade in row.items():
                if course not in ["StudentID", "Name"]:
                    student.addGrade(course, int(grade))
            
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
