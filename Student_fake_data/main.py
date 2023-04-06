from student import Student
import random


students = []
for _ in range(300):
    student = Student()
    students.append(        
        {
            "name": student.name,
            "surname": student.surname,
            "email": student.email,
            "JMBAG": student.jmbag
        }
    )

for student in students:
    print(student)
