class Student: #parent class
    def __init__(self, student_id):
        self.student_id = student_id

class QualifiedStudent(Student): #child class(inheritance)
    def check_qualification(self):
        num = int(self.student_id.split("_")[1])
        return num % 2 == 0
    
#creating 10 students using list
students = [QualifiedStudent("std_001"), QualifiedStudent("std_002"), QualifiedStudent("std_003"),
            QualifiedStudent("std_004"), QualifiedStudent("std_005"), QualifiedStudent("std_006"),
            QualifiedStudent("std_007"), QualifiedStudent("std_008"), QualifiedStudent("std_009"),
            QualifiedStudent("std_010")]

even_students = []
odd_students = []

#checking qualification
for student in students:
    if student.check_qualification():
        even_students.append(student.student_id)
    else:
        odd_students.append(student.student_id)

#convert to tuple
even_students = tuple(even_students)
odd_students = tuple(odd_students)

#displaying results
print("Students allowed to participate first(Even ROLL_ID's):")
print(even_students)

print("\nStudents allowed to participate later(Odd ROLL_ID's):")
print(odd_students)