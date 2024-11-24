class Book:
    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

        # Open the file in append mode to avoid overwriting data
        with open("library.txt", "r+") as f:
            content = f.read()
            # Check if the book already exists in the file
            if f"Title:{self.title}" not in content or f"Author:{self.author}" not in content:
                f.write(f"Title:{self.title}\nAuthor:{self.author}\n\n")
    
    @staticmethod
    def remove_book_from_file(text_to_remove):
        # Step 1: Read all lines from the file
        with open("library.txt", "r") as file:
            lines = file.readlines()

        # Step 2: Remove lines matching the text to remove
        updated_lines = [line for line in lines if text_to_remove not in line]

        # Step 3: Write back to the file
        with open("library.txt", "w") as file:
            file.writelines(updated_lines)


class Library:
    def __init__(self):
        pass

    def add_book(self, title, author):
        # Adds a new book to the library
        Book(title, author, is_borrowed=False)
        return f"The book '{title}' by {author} has been added to the library."

    def borrow_book(self, title):
        # Borrow a book if available
        with open("library.txt", "r") as f:
            content = f.read()
            if f"Title:{title}" in content:
                Book.remove_book_from_file(f"Title:{title}")
                return f"You have borrowed the book '{title}'."
            else:
                return f"The book '{title}' is not available in the library."

    def return_book(self, title, author):
        # Return a book to the library
        Book(title, author, is_borrowed=False)
        return f"The book '{title}' has been returned to the library."

    def display_books(self):
        # Display all books in the library
        with open("library.txt", "r") as f:
            content = f.read()
        return content if content else "The library is empty."


# Main program logic
purpose = input("Do you want to return a book, borrow a book, or see the list of books? (return/borrow/list): ").lower()

if purpose == "return":
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    library = Library()
    message = library.return_book(title, author)
    print(message)

elif purpose == "borrow":
    title = input("Enter the title of the book: ")
    library = Library()
    message = library.borrow_book(title)
    print(message)

elif purpose == "list":
    library = Library()
    print("Books in the library:")
    print(library.display_books())

else:
    print("Invalid input. Please choose 'return', 'borrow', or 'list'.")
