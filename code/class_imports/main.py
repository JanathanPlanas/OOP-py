
from school_class import school_class
from student import Student

student = Student('Johns')
school_class = school_class(123)
school_class.add_student(student)
print(school_class.show_class())
