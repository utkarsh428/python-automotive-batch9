def calculator(func):
    def wrapper(a, b, operation):
        operations = {
            "add": a + b,
            "sub": a - b,
            "mul": a * b,
            "div": a / b if b != 0 else "undefined (division by zero)"
        }
        result = operations.get(operation.lower(), "invalid operation")
        print(f"Result: {result}")
        return func(a, b, operation)
    return wrapper

@calculator
def calculate(a, b, operation):
    pass

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Choose operation (add, sub, mul, div): ")
calculate(a, b, operation)