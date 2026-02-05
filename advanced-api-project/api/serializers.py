from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

#BookSerializer: Serializes Book model data.Includes validation to prevent future publication years.
class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = '__all__'

  def validate_publication_year(self, value):
    """Ensures the publication year is not in the future""" 
    current_year = datetime.now().year
    if value > current_year:
      raise serializers.ValidationError(
        "Publication year cannot be in the future."
      )
    return value
  
class AuthorSerializer(serializers.ModelSerializer):
  """Serializes Author data along with related books.
  Uses a nested BookSerializer to represent the one-to-many relationship.""" 
  books = BookSerializer(many=True, read_only=True)

  class Meta:
    model = Author
    fields = ['id', 'name', 'books']
  