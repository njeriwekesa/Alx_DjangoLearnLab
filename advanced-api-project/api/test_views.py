from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from api.models import Author, Book

# Django automatically uses a separate test database when running manage.py test


class BookAPITestCase(APITestCase):
  """
  Test suite for Book API endpoints.
  Covers CRUD operations, authentication and permissions.
  """

  def setUp(self):
    #Create user for authenticated requests
    self.user = User.objects.create_user(
      username="testuser",
      password="testpassword"
    )

    self.client = APIClient()

    #create sample author and book
    self.author = Author.objects.create(name="Test Author")
    self.book = Book.objects.create(
      title="Test Book",
      publication_year=2020,
      author=self.author
    )

    self.book_list_url = "/api/books/"
    self.book_detail_url = f"/api/books/{self.book.id}/"


  def test_get_books_list(self):
    """Test retrieving list of books"""
    response = self.client.get(self.book_list_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertIsInstance(response.data, list)

  def test_create_book_requires_authentication(self):
    """Test that unauthenticated users cannot create books"""  
    data = {
      "title": "New Book",
      "publication_year": 2022,
      "author": self.author.id
    }
    response = self.client.post(self.book_list_url, data)
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


  def test_create_book_authenticated(self):
    """Test creating a book with authentication"""  
    self.client.force_authenticate(user=self.user)

    data = {
      "title": "Authenticated Book",
      "publication_year": 2021,
      "author": self.author.id
    }
    response = self.client.post(self.book_list_url, data)
    self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

  def test_update_book(self):
    """Test updating a book"""  
    self.client.force_authenticate(user=self.user)

    data = {
      "title": "Updated Title",
      "publication_year": 2019,
      "author": self.author.id
    }
    response = self.client.put(self.book_detail_url, data)
    self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

  def test_delete_book(self):
    """Test deleting a book"""
    self. client.force_authenticate(user=self.user)

    response = self.client.delete(self.book_detail_url)
    self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)