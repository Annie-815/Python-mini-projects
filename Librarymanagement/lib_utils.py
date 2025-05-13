print("Library utilities successfully loaded")
def add_book(library, book_title):
   if book_title in library:
      print(f"{book_title} is already in the library")
   else:
      library[book_title] = True
      print(f"{book_title} successfully added to the library")

def remove_book(library, book_title):
   if book_title in library:
      del library[book_title]
      print(f"{book_title} successfully deleted from the library")
def display_books(library):
   if not library:
      print("The library does not exist")
   else:
      print("Books currently available")
      for book in library:
         print(f" - {book}")