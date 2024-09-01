from relationship_app.models import Author, Book, Library, Librarian


# query all books by a specific author
author = Author.objects.get(name='John Doe')
books = Book.objects.filter(author=author)
print(books)


#List all books in the library
library = Library.objects.get(name='Main Library')
books = library.books.all()
print(books)


# Retrive the librarian of a library
library = Library.objects.get(name='Main Library')
librarian = library.librarian
print(librarian.name)

