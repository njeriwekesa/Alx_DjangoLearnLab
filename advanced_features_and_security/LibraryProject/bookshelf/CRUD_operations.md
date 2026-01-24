# CRUD Operations for Book Model

This document demonstrates Create, Retrieve, Update, and Delete (CRUD) operations
performed on the Book model using the Django shell.

---

## Create

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

book
##<Book: 1984>


##Retrieve

from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
##('1984', 'George Orwell', 1949)


##Update

from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book
##<Book: Nineteen Eighty-Four>

##Delete

from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()

##<QuerySet []>

