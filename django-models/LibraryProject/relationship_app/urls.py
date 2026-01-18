from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, LibraryDetailView, add_book, edit_book, delete_book


urlpatterns = [
  path('books/', list_books, name='list_books'),
  path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), 

  #Auth URLs
  path('register/', views.register, name='register'),
  path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
  path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

  #UserProfile URLs
  path('admin/', views.admin_view, name='admin_view'),
  path('librarian/', views.librarian_view, name='librarian_view'),
  path('member/', views.member_view, name='member_view'),

  #add, edit, delete Book URLs
  path('add_book/', add_book, name='add_book'),
  path('edit_book/<int:pk>/edit/', edit_book, name='edit_book'),
  path('delete_book/<int:pk>/delete/', delete_book, name='delete_book'),
]