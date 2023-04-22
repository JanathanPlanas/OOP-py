
from student import Student


class school_class:

    def __init__(self, class_code) -> None:

        self.code = class_code
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def show_class(self):
        return self.students


