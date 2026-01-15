from relationship_app.models import Author, Book, Library, Librarian

#Query all books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = author.books.all()

#list all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()

#retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
