try:
    n = int(input())

    if n <= 0:
        print("Error: The length of the list must be a non-negative integer.")
    exit()
    

    total = 0

    for _ in range(n):
        total += int(input())

    avg = total / n
    print(f"The average is: {avg:.2f}")

except ValueError:
    print("Error: You must enter a numeric value.")