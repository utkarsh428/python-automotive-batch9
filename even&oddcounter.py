even = odd = 0
i = 0
while i < 10:
    n = int(input("Enter number: "))
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    i += 1
    print(f"Even: {even}, Odd: {odd}")