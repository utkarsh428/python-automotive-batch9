def main():
# Get list length
    while True:
        n_input = input("Enter the length of the list (n): ").strip()
# validate that n is a positive integer
        if n_input.isdigit():
            n = int(n_input)
            if n < 0:
                print("Error: The length of the list must be a non-negative integer.")
                continue
            break
        else:
            print("Error: The length of the list must be a non-negative integer.")
    
    if n == 0:
        print("The list is empty. Average cannot be calculated.")
        return
    
    # Collect n integers from user
    numbers = []
    for i in range(1, n + 1):
        while True:
            elem_input = input(f"Enter element {i}: ").strip()
            if elem_input.lstrip('-').isdigit():
                numbers.append(int(elem_input))
                break
            else:
                print("Error: You must enter a numeric value.")
    
    # Calculate and print average
    average = sum(numbers) / n
    print(f"The average of the list is: {average:.2f}")

if __name__ == "__main__":
    main()