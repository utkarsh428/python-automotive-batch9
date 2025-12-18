def is_pass(marks):
    if marks >=60:
        return True
    else:
        return False
    
    def progress_report(physics, chemistry, maths):

        if is_pass(physics) and is_pass(chemistry) and is_pass(maths):
            return True
        else:
            return False
        
        physics = int(input("Enter physics marks: "))
        chemistry = int(input("Enter chemistry marks: "))
        maths = int(input("Enter maths marks: "))

        result = progress_report(physics, chemistry, maths)

        if result:
             print("Overall Result:PASS")
        else:
             print("Overall Result:FAIL")