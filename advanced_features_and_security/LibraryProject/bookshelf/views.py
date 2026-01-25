from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import authenticate, login
from .models import Book
from .forms import ExampleForm



# view/create/edit/delete Book decorators to enforce these permissions

# @permission_required('bookshelf.can_create', raise_exception=True)
# def add_book(request):
#   if request.method == "POST":
#     title = request.POST.ger("title")
#     author = request.POST.get("author")
#     year = request.POST.get("publication_year")

#     Book.objects.create(
#       title=title,
#       author=author,
#       publication_year=year
#     )

#     return HttpResponse("Book created successfully")
  
#   return HttpResponse("Send a POST request to create a book")

@permission_required('bookshelf.can_create', raise_exception=True)
def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Book added successfully")
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

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
def book_list(request):
  books = Book.objects.all()

  #output = ", ".join(book.title for book in books)
  return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
  book = get_object_or_404(Book, pk=pk)
  book.delete()

  return HttpResponse("Book deleted successfully")


def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("book_list")  
        
        else:
            error = "Invalid username or password"

    return render(request, "bookshelf/login.html", {"error": error})


