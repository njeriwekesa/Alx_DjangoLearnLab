from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer


# BookList
class BookList(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
  querryset = Book.objects.all()
  serializer_class = BookSerializer