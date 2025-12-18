#func to add two numbers
def add(a,b):
    return a + b
#func to subtract two numbers
def sub(a,b):
    return a - b
#func to multiply two numbers
def mul(a,b):
    return a * b
#func to divide two numbers
def div(a,b):
    return a/b

#taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nchoose operation \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide")
choice = input("Enter choice(1/2/3/4): ")

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", sub(num1, num2))
elif choice == '3':
    print("Result:", mul(num1, num2))
elif choice == '4':
    print("Result:", div(num1, num2))
else:
    print("Invalid choice")