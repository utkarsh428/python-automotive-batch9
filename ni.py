def main():
    # Get list length
    while True:
        n_input = input("Enter the length of the list (n): ").strip()
        try:
            if n_input.isdigit():
                n = int(n_input)
                if n < 0:
                    print("Error: The length of the list must be a non-negative integer.")
                    continue
                break
            else:
                print("Error: The length of the list must be a non-negative integer.")
        except ValueError:
            print("Error: Invalid input for list length.")

    if n == 0:
        print("The list is empty. Average cannot be calculated.")
        return

    # Collect n integers from user
    numbers = []
    for i in range(1, n + 1):
        while True:
            elem_input = input(f"Enter element {i}: ").strip()
            try:
                if elem_input.lstrip('-').isdigit():
                    numbers.append(int(elem_input))
                    break
                else:
                    print("Error: You must enter a numeric value.")
            except ValueError:
                print("Error: Invalid numeric input.")
    # Calculate and print average
    try:
        average = sum(numbers) / n
        print(f"The average of the list is: {average:.2f}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid data for average calculation.")


if __name__ == "__main__":
    main()