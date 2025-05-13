# Make sure you have a file named library_utils.py
import lib_utils as lib_utils

library = {}
try:
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Exit")

        choice = input("Enter your choice of operation 1-4: ").strip()
        print(f"DEBUG: User entered: {repr(choice)}")

        if choice == "1":
            title = input("Enter the title of the book you want to add: ").strip()
            lib_utils.add_book(library, title)

        elif choice == "2":
            title = input("Enter the title of the book you want to remove: ").strip()
            lib_utils.remove_book(library, title)

        elif choice == "3":
            lib_utils.display_books(library)

        elif choice == "4":
            print("You have exited the system. Goodbye!")
            break

        else:
            print("The choice you have entered is not available. Please enter a number between 1 and 4.")
except Exception as e:
    print("An error occurred:", e)