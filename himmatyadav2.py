# Addition function
def add(x, y):
    return x + y

# Subtraction function
def subtract(x, y):
    return x - y

# Multiplication function
def multiplication(x, y):
    return x * y

# Division function
def division(x, y):
    if y == 0:
        return "Error! Division by zero"
    else:
        return x / y

# Calculator function
def calculator():
    x = int(input("Enter 1st number: "))
    y = int(input("Enter 2nd number: "))

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        print("Result of addition is: ", add(x, y))
    elif choice == 2:
        print("Result of subtraction is: ", subtract(x, y))
    elif choice == 3:
        print("Result of Multiplication: ", multiplication(x, y))
    elif choice == 4:
        print("Result of Division is: ", division(x, y))
    else:
        print("ohh you choose any Invalid choice!")


# Call calculator
calculator()