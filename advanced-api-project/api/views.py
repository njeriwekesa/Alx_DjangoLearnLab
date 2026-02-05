from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

"""
ListView retrieves a list of books. 
Accessible to both authenticated and unauthenticated users
"""
class BookListView(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [permissions.AllowAny]


"""
DetailView retrieves a single book by its ID.
Accessible to both authenticated and unauthenticated users.
"""
class BookDetailView(generics.RetrieveAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [permissions.AllowAny]


"""
CreateView creates a new book entry.
Restricted to authenticated users only.
"""
class BookCreateView(generics.CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [permissions.IsAuthenticated]


"""
UpdateView updates an existing book.
Restricted to authenticated users only.
"""  
class BookUpdateView(generics.UpdateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [permissions.IsAuthenticated]


"""
DeleteView deletes a book.
Restricted to authenticated users only.
"""  
class BookDeleteView(generics.DestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [permissions.IsAuthenticated]