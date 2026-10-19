
class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_name):
        if book_name in self.books:
            print("Book already exists.")
        else:
            self.books[book_name] = True
            print("Book added successfully.")

    def remove_book(self, book_name):
        if book_name not in self.books:
            print("Book not found.")
        elif not self.books[book_name]:
            print("Book is currently issued. Return it first.")
        else:
            del self.books[book_name]
            print("Book removed successfully.")

    def issue_book(self, book_name):
        if book_name not in self.books:
            print("Book not found.")
        elif not self.books[book_name]:
            print("Book is already issued.")
        else:
            self.books[book_name] = False
            print("Book issued successfully.")

    def return_book(self, book_name):
        if book_name not in self.books:
            print("Book not found.")
        elif self.books[book_name]:
            print("This book was not issued.")
        else:
            self.books[book_name] = True
            print("Book returned successfully.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nLibrary Books:")
            for name, available in self.books.items():
                status = "Available" if available else "Issued"
                print(name, "-", status)


library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        book_name = input("Enter book name: ").strip()
        if book_name:
            library.add_book(book_name)
        else:
            print("Book name cannot be empty.")

    elif choice == "2":
        book_name = input("Enter book name to remove: ").strip()
        library.remove_book(book_name)

    elif choice == "3":
        book_name = input("Enter book name to issue: ").strip()
        library.issue_book(book_name)

    elif choice == "4":
        book_name = input("Enter book name to return: ").strip()
        library.return_book(book_name)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
