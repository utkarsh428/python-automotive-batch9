while True:
    print("1. square 2. cube 3.exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        n = int(input("number:"))
        print(n * n)
    elif choice == 2:
        n = int(input("number:"))
        print(n * n * n)
    elif choice == 3:
        break
    else:
        print("invalid choice")