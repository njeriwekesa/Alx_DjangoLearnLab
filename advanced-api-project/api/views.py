from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

"""
ListView retrieves a list of books. 
Accessible to both authenticated and unauthenticated users
"""
class BookListView(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]


"""
DetailView retrieves a single book by its ID.
Accessible to both authenticated and unauthenticated users.
"""
class BookDetailView(generics.RetrieveAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]


"""
CreateView creates a new book entry.
Restricted to authenticated users only.
"""
class BookCreateView(generics.CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]


"""
UpdateView updates an existing book.
Restricted to authenticated users only.
"""  
class BookUpdateView(generics.UpdateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]


"""
DeleteView deletes a book.
Restricted to authenticated users only.
"""  
class BookDeleteView(generics.DestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated]