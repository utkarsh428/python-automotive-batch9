try:
    
    file = open("users.txt", "r")
    data = file.read()

    #checks whether the file is empty using strip()
    if data.strip() == "":
        print("The file is empty.")
    else:
        print("User Data:")
        print(data)

    file.close()

#if the file does not exist
except FileNotFoundError:
    print("Error: File not found.")

#the file is handled using exception
except Exception:
    print("Error: File is corrupted or unreadable.")

finally:
    print("Program continues running smoothly.")
