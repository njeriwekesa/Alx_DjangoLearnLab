from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


from .models import Book
from .serializers import BookSerializer

"""
ListView retrieves a list of books with support for filtering, searching and ordering.
Read-only access for unauthenticated users
"""
class BookListView(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

  #Enable filtering, searching, ordering
  filter_backends = [
    DjangoFilterBackend,
    SearchFilter,
    OrderingFilter,
  ]

  #Filtering (exact matches)
  filterset_fields = ['title','publication_year', 'author']

  #searching (partial text match)
  search_fields = ['title', 'author__name']

  # Ordering
  ordering_fields = ['title', 'publication_year']
  ordering = ['title'] #default order



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