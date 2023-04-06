from student import Student
import json


students = []
for _ in range(300):
    student = Student()
    students.append(        
        {
            "name": student.name,
            "surname": student.surname,
            "email": student.email,
            "JMBAG": student.jmbag,
            "course_id": student.courseID
        }
    )

with open("./Student_fake_data/students.json", "w") as file:
    json.dump(students, file)
