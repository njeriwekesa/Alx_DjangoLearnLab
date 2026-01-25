from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book

# view/create/edit/delete Book decorators to enforce these permissions

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
  if request.method == "POST":
    title = request.POST.ger("title")
    author = request.POST.get("author")
    year = request.POST.get("publication_year")

    Book.objects.create(
      title=title,
      author=author,
      publication_year=year
    )

    return HttpResponse("Book created successfully")
  
  return HttpResponse("Send a POST request to create a book")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
  book = get_object_or_404(Book, pk=pk)

  if request.method == "POST":
    book.title = request.POST.get("title")
    book.author = request.POST.get("author")
    book.publication_year = request.POST.get("publication_year")
    book.save()

    return HttpResponse("Book updated successfully")
  
  return HttpResponse(f"Editing book: {book.title}")

@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
  books = Book.objects.all()

  output = ", ".join(book.title for book in books)
  return HttpResponse(f"Books: {output}")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
  book = get_object_or_404(Book, pk=pk)
  book.delete()

  return HttpResponse("Book deleted successfully")