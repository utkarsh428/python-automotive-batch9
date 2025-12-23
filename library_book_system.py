class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True   
# Book is available initially

    def issue_book(self):
        if self.is_available:
            self.is_available = False
            print("Book issued successfully")
        else:
            print("Book already issued")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print("Book returned successfully")
        else:
            print("Book was not issued")

    def display_status(self):
        print("\nBook ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Status:", "Available" if self.is_available else "Issued")


# Taking user input
book_id = int(input("Enter Book ID: "))
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")

# Create Book object
book = Book(book_id, title, author)

# Menu to check book operations
while True:
    print("\n1. Issue Book")
    print("2. Return Book")
    print("3. Display Status")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book.issue_book()
    elif choice == "2":
        book.return_book()
    elif choice == "3":
        book.display_status()
    elif choice == "4":
        print("Exiting program")
        break
    else:
        print("Invalid choice")