def is_pass(marks): #this checks whether the marks are 60 or more 
    #it returns true if yes and false if no
    return marks>=60

#taking input for three subjects
Compute_Science = int(input("Computer Science marks: "))
ML = int(input("ML marks: "))
DSA = int(input("DSA marks: "))

#is_pass() returns true or false based on marks
print("Computer Science:", "Pass" if is_pass(Compute_Science) else "Fail")
print("ML:", "Pass" if is_pass(ML) else "Fail")
print("DSA:", "Pass" if is_pass(DSA) else "Fail")