class Book:
    def __init__(self,title,author,is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        with open("library.txt" , "w" ,"r") as f:
            if {self.title} in f.read() and {self.author} in f.read():
               pass
            else:
               f.write(f'''Title:{self.title}.
                    Author:{self.author}
{self.is_borrowed} \n''')
    
    def class_borrow_book(self):
        return 
        
    def return_book(self):
        return self.is_borrowed == False
    
    def remove_book_from_file( title_to_remove):
        # Step 1: Read all lines from the file
        with open("library.txt", "r") as file:
            lines = file.readlines()

        # Step 2: Filter out the line containing the book title to remove
            updated_lines = [line for line in lines if not line.startswith(title_to_remove)]

        # Step 3: Write the updated list back to the file
        with open("library.txt", "w") as file:
            file.writelines(updated_lines)


           
            

class Library(Book):
  
    
    def add_book(self):
        return f'''The title of book is {self.title}.
    The author of book is "{self.author}"'''
       
    def borrow_book(self , title):
         with open("library.txt" , "r") as f:
             if self.title in f.read :
                 return f"{self.title} is not available."
     
    def return_book(self , title):
         with open("library.txt" , "r") as f:
            if self.title in f.read :
                 return f"{self.title} is available ."

        
    def display_book(self):
        with open("library.txt" , "r") as f:
           print(f.read())


purpose = input("DO you want to return a book or borrow a book or DO you want to see list of books in library? (return/borrow/list) ::")
if purpose.lower() == "return" :
    title = input("Enter the title of book : ")
    author = input("Enter the author of book :")
    library = Library()
    availability = library.borrow_book()
    book_return = Book(title , author , availability)
    book_return.remove_book_from_file(f"Title:{title}")
    book_return.remove_book_from_file(f"Author:{author}")

elif purpose.lower() == "return" :
    title = input("Enter the title of book : ")
    author = input("Enter the author of book : ")
    library = Library()
    availability = library.return_book()
    book_return = Book(title , author ,  availability )

elif purpose.lower() == "list":
    library = Library("h", "j" , "k")
    print(library.display_book())    

