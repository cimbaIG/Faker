from student import Student
from  faker import Faker
import random


# Function to generate random number for a given number of digits
def randomDigits(digits):
    lower = 10**(digits-1)
    upper = 10**digits - 1
    return random.randint(lower, upper)

# Remove Croatian letters from string
def remove_croatian_letters(string: str):
    string = string.lower()
    letters = {
        "č": "c", 
        "ć": "c", 
        "š": "s", 
        "ž": "z",
        "dž": "dj", 
        "đ": "dj"
        }
    for letter in string:
        if letter in letters.keys():
            string = string.replace(letter, letters[letter])
            
    return string

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