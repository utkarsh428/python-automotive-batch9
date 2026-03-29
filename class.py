
class Student:    
    def __init__(self): #init method is a constructor
        self.name = "Student" #it will store student name
        self.marks = 30 #it will store student marks

    def study(self):
        print("student is studying")

    def display(self):
        print("Name:", self.name) #display name
        print("Marks:", self.marks) #display marks

    def result(self):
        if self.marks >= 40:
            print("Student is Pass")
        else:
            print("Student is Fail")

s1 = Student()  #creating object for student class
#calling methods
s1.study()
s1.display()
s1.result()