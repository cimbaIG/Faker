from faker import Faker
import random


class Student:
    
    CRO_LETTERS = {
            "č": "c", 
            "ć": "c", 
            "š": "s", 
            "ž": "z",
            "dž": "dj", 
            "đ": "dj"
            }
    
    def __init__(self):
        
        fake_data = Faker('hr_HR')
        
        self._name = fake_data.unique.name().split(' ')[0]
        self._surname = fake_data.unique.name().split(' ')[1]
        self._email = self.generate_email()
        self._jmbag = self.generate_jmbag(10)
        
    @property
    def name(self):
        return self._name
    
    @property
    def surname(self):
        return self._surname
    
    @property
    def email(self):
        return self._email
    
    @property
    def jmbag(self):
        return self._jmbag
    
    def __str__(self):
        return f"Student {self._jmbag}, "+ f"{self._name}" + " " \
            + f"{self._surname}," + f" {self._email}"
            
    def generate_jmbag(self, num_of_digits: int):
        lower = 10**(num_of_digits-1)
        upper = 10**num_of_digits - 1
        return random.randint(lower, upper)
    
    def remove_croatian_letters(self, string: str):
        string = string.lower()
        
        for letter in string:
            if letter in Student.CRO_LETTERS.keys():
                string = string.replace(letter, Student.CRO_LETTERS[letter])
                
        return string
    
    def generate_email(self):
        return self.remove_croatian_letters(self.name) + "." \
            + self.remove_croatian_letters(self.surname) + "@fsb.hr"