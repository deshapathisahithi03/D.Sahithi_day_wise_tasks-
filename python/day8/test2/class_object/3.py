class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        
    def display_book(self):
        print(f"the title of the book is:{self.title}")
        print(f"the author of the book is:{self.author}")
        print(f"the isbn of the book is:{self.isbn}")
        
book=Book("Ramayana","Valmiki","56A34")
book.display_book()
        