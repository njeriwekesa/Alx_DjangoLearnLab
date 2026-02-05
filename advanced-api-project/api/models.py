from django.db import models

# Author model: represents a book author. An author can be associated with multiple books.
class Author(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name


"""
Book Model: represents a book written by an author. Each book is linked to one author, forming a one-to-many relationship.
"""
class Book(models.Model):
  title = models.CharField(max_length=255)
  publication_year = models.IntegerField()
  author = models.ForeignKey(
    Author,
    related_name = 'books',
    on_delete =  models.CASCADE
  )

  def __str__(self):
    return self.title