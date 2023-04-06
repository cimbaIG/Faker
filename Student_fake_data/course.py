from random import randint


class Course:
    
    COURSES = {
        0: "Mehanika fluida",
        1: "Mehanika fluida 1",
        2: "Mehanika fluida K",
        3: "Mehanika fluida 2",
        4: "Dinamika plinova"
    }
    
    def __init__(self):
        self._course_id = randint(0,4)
        self._course_name = Course.COURSES[self._course_id]
        
    @property
    def course_id(self):
        return self._course_id
        
    @property
    def course_name(self):
        return self._course_name