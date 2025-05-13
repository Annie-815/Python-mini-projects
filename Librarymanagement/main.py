import lib_utils
library = {}

while True:
    print("Library management system")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Display Books")
    print("4. Exit")

    choice = input("Enter your choice of operation 1-4: ").strip()
    if choice == "1":
        title = input("enter the title of the book you want to add").strip()
        lib_utils.add_book(library, title)
    elif choice == "2":
        title = input("Enter the title of the book you want to delete").strip()
        lib_utils.remove_book(library, title)
    elif choice == "3":
        lib_utils.display_books(library)
    elif choice == "4":
        print("You have exited the system")
        break
    else:
        print("the choice you have entered is not available")