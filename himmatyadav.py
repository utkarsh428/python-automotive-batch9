def result_card():
    # Take marks from user
    maths = int(input("Enter Maths marks: "))
    science = int(input("Enter Science marks: "))

    # Check Maths result
    if maths >= 60:
        print("You have passed in Maths")
    else:
        print("You have failed in Maths")

    # Check Science result
    if science >= 60:
        print("You have passed in Science")
    else:
        print("You have failed in Science")

# Calling the function
result_card()