from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import register_view

urlpatterns = [
  path('books/', list_books, name='list_books'),
  path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 

  #Auth URLs
  path('register/', register_view, name='register'),
  path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
  path('logout/', LogoutView.as_view('relationship_app/logout.html'), name='logout'),
]
