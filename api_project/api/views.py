from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer


# BookList
class BookList(generics.ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticated] #--> BookViewSet uses TokenAuthentication (configured in settings.py). Only authenticated users can perform CRUD operations
